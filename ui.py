
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QFrame, QLabel, QTableWidgetItem, QGridLayout
from PyQt5.QtGui import QPixmap, QBrush, QColor, QIcon, QPalette
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QThread, QPoint, QRectF, QSize, Qt, QTimer

from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QFrame, QLabel, QTableWidgetItem
from PyQt5.QtGui import QPixmap, QBrush, QColor, QIcon
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QThread,QPoint, QRectF, QSize, Qt, QTimer
from qtDataframe import IQDataFrameWidget
from numpy import NaN

from time import sleep, time
#import qdarkstyle
import qdarktheme
import sys
import os
from pandas import DataFrame, Series
from Track import Track
from Recorder import recorder
from Player import player
from titlebar_qt import TitleBar
import pynput
import logging
from QtimeEdite import tmanip
from Hotkey import hotkey
from PV import DFV
logging.basicConfig(filename="GCM.log",filemode="w",
     format='%(levelname)s:%(name)s:%(lineno)s:  %(message)s', level=logging.INFO)

gen = 0
if __name__ == '__main__':
    if gen:
        os.system("pyuic5 -x OGC_ui.ui -o OGC_ui.py")
        os.system("pyrcc5 image.qrc -o image_rc.py")
import OGC_ui


class Worker(QObject):### U interface
    rec_stoped_sig = pyqtSignal(str)
    play_stop_sig = pyqtSignal()
    play_pause_sig = pyqtSignal()
    play_stoped_sig = pyqtSignal()
    setBusyFlag_sig = pyqtSignal(str, bool)
    start_sig = pyqtSignal(str, int, tmanip)
    save_sig = pyqtSignal(str)
    autoRel_sig = pyqtSignal(bool)
    setTime_sig = pyqtSignal(float)
    rstTime_sig = pyqtSignal()
    expIm_sig = pyqtSignal(str)
    screendir_sig = pyqtSignal(str)
    progress_sig = pyqtSignal(str, float)
    stackPrev_sig = pyqtSignal()
    stackNext_sig = pyqtSignal()


    def __init__(self):
        super(Worker, self).__init__()
        self.mouse = pynput.mouse.Controller()
        self.key = pynput.keyboard.Controller()
        self.rec = recorder(self.mouse, self.key)
        self.Player = player(self.mouse, self.key)
        self.stack = {}
        self.currentTrack = None
        self.start_sig.connect(self.start)
        self.save_sig.connect(self.saveCurrentTrack)
        self.play_pause_sig.connect(self.pause)
        self.play_stop_sig.connect(self.stop)
        self.stoprepeat=1
        self.expIm_sig.connect(self.exportImgs)
        self.screendir_sig.connect(self.screenshotDir)
        self.stackNext_sig.connect(self.stackNext)
        self.stackPrev_sig.connect(self.stackPrev)
        self.timeStepBetweenTrack=0

    @pyqtSlot()
    def stackPrev(self):
        if self.currentTrack in self.stack:
            self.setBusyFlag_sig.emit("stack", True)
            self.stack[self.currentTrack].stack_prev()
            self.setBusyFlag_sig.emit("stack", False)

    @pyqtSlot()
    def stackNext(self):
        if self.currentTrack in self.stack:
            self.setBusyFlag_sig.emit("stack", True)
            self.stack[self.currentTrack].stack_next()
            self.setBusyFlag_sig.emit("stack", False)

    @pyqtSlot(str)
    def exportImgs(self, path):
        self.stack[self.currentTrack].exportImgs(path,callbackProg=self.progress_sig.emit)

    @pyqtSlot(bool)
    def auto_relto(self, flag):
        self.stack[self.currentTrack].auto_relto(flag)

    @pyqtSlot(int)
    def screenshotAtRelease(self, flag):
        if self.currentTrack in self.stack:
            self.stack[self.currentTrack].screenshotAtRelease(flag)
    
    @pyqtSlot(str)
    def screenshotDir(self,path):
        self.Player.screenshotAtClick(self.Player.screenshot, path)

    @pyqtSlot(int)
    def screenshotAtClick(self,flag):
        self.Player.screenshotAtClick(flag)
    
    @pyqtSlot(int)
    def imPesistancy(self, _max):
        self.Player.imPesistancy=_max

    @pyqtSlot(str)
    def saveCurrentTrack(self, path):
        self.stack[self.currentTrack].save(path)

    @pyqtSlot(str)
    def renameCurrentTrack(self, name):
        t = self.stack.pop(self.currentTrack)
        t.rename(name)
        self.stack[name] = t
        self.currentTrack = name
        logging.info("Worker renameCurrentTrack "+name)

    @pyqtSlot(str)
    def setCurrentTrack(self, name):
        if name != "Add Track":
            self.setBusyFlag_sig.emit("currentTrack", True)
        if (not name in self.stack) and (name != "Add Track"):
            t = Track(name)
            self.currentTrack = t.name
            self.stack[t.name] = t
        elif name != "Add Track":
            self.currentTrack = name
        if name != "Add Track":
            self.setBusyFlag_sig.emit("currentTrack", False)

    @pyqtSlot()
    def rmCurrentTrack(self):
        if self.currentTrack in self.stack:
            ret = self.stack.pop(self.currentTrack)
            del ret

    @pyqtSlot(str, int, int)
    def recStart(self, name, autoRel, screenshot):
        if name in self.stack and self.rec.statu == "stop":
            self.setBusyFlag_sig.emit("Rstart", True)
            self.auto_relto(autoRel)
            self.screenshotAtRelease(screenshot)
            self.rec.start(self.stack[self.currentTrack])
            # something

    @pyqtSlot()
    def recStop(self):
        if self.rec.stop():
            self.stack[self.currentTrack].stack_next(1)
            self.setBusyFlag_sig.emit("Rstart", False)

    @pyqtSlot()
    def pause(self):
        print("set pause")
        if self.Player.statu == "start":
            self.Player.pause()
            self.setBusyFlag_sig.emit("Ppause", False)

    @pyqtSlot(str, int, tmanip)
    def start(self, name, Ch_rp_p_repeat_checkState, Qtedit):
        if (name in self.stack) and (self.Player.statu == "stop" or self.Player.statu == "pause"):
            self.setBusyFlag_sig.emit("Pstart", True)
            ###
            if self.Player.statu == "pause":
                self.Player.start()
                return 0
            self.stoprepeat=0
            t0=time()-self.timeStepBetweenTrack
            if Ch_rp_p_repeat_checkState:
                while Qtedit.decrem() and self.stoprepeat==0:
                    while time()-t0<self.timeStepBetweenTrack:
                        sleep(0.01)
                    self.Player.start(self.stack[self.currentTrack])################
                    t0=time()
                    while self.Player.statu!='stop':
                        sleep(0.01)
                self.stoprepeat=0
            else:
                self.Player.start(self.stack[self.currentTrack])
            # something
            if self.Player.statu == "stop":
                self.setBusyFlag_sig.emit("Pstart", False)
                self.play_stoped_sig.emit()
                return 0

    @pyqtSlot()
    def stop(self):
        if self.Player.statu != "stop":
            self.stoprepeat=1
            self.Player.stop()

class OGC(QMainWindow, OGC_ui.Ui_MainWindow):### G interface
    setTrack_sig = pyqtSignal(str)
    renameTrack_sig = pyqtSignal(str)
    removeTrack_sig = pyqtSignal()

    def dragEnterEvent(self, e):
        txt = e.mimeData().text()
        if ".ogc" in txt:
            e.accept()
        else:
            e.ignore() 

    def dropEvent(self, e):
        self.MultiImport(e.mimeData().text().replace("file:///", "").split("\n"))

    def MultiImport(self, listPath):
        self.set_busy_flag("currentTrack", True)
        for path in listPath:
            if "\\" in path or "/" in path or ":" in path:
                self.worker.setCurrentTrack(path)
                self.worker.stack[self.worker.currentTrack].path=path
                self.IDfTable.QTable.setCurrentCell(self.IDfTable.QTable.rowCount()-1,0)
                self.IDfTable.QTable.item(self.IDfTable.QTable.rowCount()-1,0).setText(self.worker.currentTrack)
        self.IDfTable.clk()
        self.set_busy_flag("currentTrack", False)


    def __init__(self, parent=None, debug=None):
        self.app = QApplication(sys.argv)
        qdarktheme.setup_theme("dark")
        super(OGC, self).__init__(parent)
        self.setupUi(self)
        if debug:
            self.DBg = DFV(self)
        else:
            self.DBg = None
        ### flag and option
        self.flag = {"checkAddRC": False, "im_rot90": 0, "refresh": 0}
        self.tmp=[]
        self.main()

    def set_busy_flag(self, key, status):
        self.flag[key] = status
        logging.info("set_busy_flag "+key+" "+str(status))
        if key == "checkAddRC":
            pass
        if key == "Pstart":
            if status:
                logging.info("start player")

                self.play_time_sig.start(100)

                self.play_time_sig.start(20)
                self.worker.Player.TimeArrayStep=0.045

            else:
                logging.info("stop or pause player")
                self.play_time_sig.stop()
                # self.showTime("p")
        if key == "Ppause":
            if status:
                pass
            else:
                logging.info("start pause")
                self.play_time_sig.stop()
        if key == "Rstart":
            if status:
                logging.info("start record")
                self.hk.stop()
                self.rec_time_sig.start(100)
                #self.tmp.append((self.IDfTable.getDataFrame(),self.IDfTable.QTable.currentRow()))
                #self.IDfTable.connections(False)
            else:
                #self.IDfTable.setDataFrame(self.tmp[0][0],0)
                #self.IDfTable.QTable.setCurrentCell(self.tmp[0][1],0)
                #self.IDfTable.connections(True)
                logging.info("stop record")
                self.rec_time_sig.stop()
                try:
                    ret = int(
                        self.worker.stack[self.worker.currentTrack].index.max())
                    if self.DBg and self.DBg.isVisible():
                        self.DBg.setMe(self.worker.stack[self.worker.currentTrack])
                except ValueError:
                    ret = 0
                self.setMaxTimeProg(ret)
                self.Qtedit.setfromsec(ret,True)
                self.hk.start()
                self.B_undo.setEnabled(self.worker.stack[self.worker.currentTrack].stack_interval[0])
                self.B_redo.setEnabled(self.worker.stack[self.worker.currentTrack].stack_interval[2])

        if key == "stack":
            if status:
                pass
            else:
                self.B_undo.setEnabled(self.worker.stack[self.worker.currentTrack].stack_interval[0])
                self.B_redo.setEnabled(self.worker.stack[self.worker.currentTrack].stack_interval[2])
                try:
                    ret = int(self.worker.stack[self.worker.currentTrack].index.max())
                except ValueError:
                    ret = 0
                self.setMaxTimeProg(ret)
                self.Qtedit.setfromsec(ret,True)

        if key == "currentTrack":
            if status:
                pass
            else:
                logging.info("Current track "+self.worker.currentTrack)
                try:
                    ret = int(self.worker.stack[self.worker.currentTrack].index.max())
                    if self.DBg and self.DBg.isVisible():
                        self.DBg.setMe(self.worker.stack[self.worker.currentTrack])
                except ValueError:
                    ret = 0
                self.B_undo.setEnabled(self.worker.stack[self.worker.currentTrack].stack_interval[0])
                self.B_redo.setEnabled(self.worker.stack[self.worker.currentTrack].stack_interval[2])
                self.setMaxTimeProg(ret)
                self.Qtedit.setfromsec(ret,True)

    def closeEvent(self, event):
        logging.info("App exit")
        self.hk.stop()
        self.thread.terminate()
        event.accept()

    def add_Track(self, name):
        logging.info("Add track "+name)
        self.setTrack_sig.emit(name)
        # df=self.IDfTable.df
        # df.loc[name]=""
        # self.IDfTable.setDataFrame(df,0)#list(self.worker.stack.keys())

    def getCurrentTrack(self):  # setCurrentTrack
        item = self.Tb_track.item(self.Tb_track.currentRow(), 0)
        if item != None:
            return item.text()

    def showTime(self, wname):
        #logging.info("set time display "+wname)
        if wname == "p":
            #logging.info("play set time display")
            if self.worker.Player.statu == "stop":
                self.setTimeProg(self.worker.Player.time)
            else:

                #self.setTimeProg(time()-self.worker.Player.t0 +
                #                 self.worker.Player.time)
                self.setTimeProg(self.worker.Player.getTimeArrayElement())
        if wname=="r":

            #logging.info("record set time display")
            self.setMaxTimeProg(time()-self.worker.rec.t0)
            self.Qtedit.setfromsec(time()-self.worker.rec.t0, True)
            self.Qtedit.setfromsec(time()-self.worker.rec.t0)

    def swapDetail(self):
        pos=self.Pb_playTime.pos()
        size=self.Pb_playTime.sizeHint()
        if not self.Gb_trackList.isHidden():
            self.B_HS.setIcon(QIcon(QPixmap(":/newPrefix/icon/down.png")))
            self.Gb_trackList.setVisible(0)
            self.W_Edit.setVisible(0)
            self.setFixedHeight(160)
            self.setFixedWidth(300)
            self.L_player_time.move(int(pos.x()+(size.width()/2)-30), int(pos.y()-4))
        else:
            self.B_HS.setIcon(QIcon(QPixmap(":/newPrefix/icon/up.png")))
            self.Gb_trackList.setVisible(1)
            self.W_Edit.setVisible(1)
            self.setFixedHeight(389)
            self.setFixedWidth(978)
            self.L_player_time.move(int(pos.x()+(size.width()/2)+70), int(pos.y()-4))

    def swapIOmode(self):
        txt=self.Tw_playRecord.tabText(self.Tw_playRecord.currentIndex())
        if txt=="Record":
            self.W_record.setVisible(True)
            self.W_play.setVisible(False)
        if txt=="Play":
            self.W_play.setVisible(True)
            self.W_record.setVisible(False)
    def setStatus(self, toPrint):
        self.L_status.setText(str(toPrint))

    def setMaxTimeProg(self, t):
        if t == 0:
            t = 0.1
        self.Pb_playTime.setRange(0, int(t*1000))
        fm, fs = divmod(t, 60)
        fh, fm = divmod(fm, 60)
        self.Pb_playTime.setValue(0)
        s, m, h = 0, 0, 0
        txt=str(int(h))+" : "+str(int(m))+" : "+str(int(s))+" / "+str(int(fh))+":"+str(int(fm))+":"+str(int(fs))
        #print(txt)
        self.L_player_time.setText(txt)
        self.L_rec_time.setText(str(int(fh))+" : "+str(int(fm))+" : "+str(int(fs)))

    def setTimeProg(self, t):
        fm, fs = divmod(t, 60)
        fh, fm = divmod(fm, 60)
        #print(self.L_player_time.text().split(" / ")[1])
        self.L_player_time.setText(str(int(fh))+" : "+str(int(fm))+" : " +str(int(fs))+" / "+self.L_player_time.text().split(" / ")[1])
        self.Pb_playTime.setValue(int(t*1000))
        self.L_player_time.show()

    def repeat(self):
        if self.Ch_rp_p_repeat.checkState():
            self.Cb_rp_p_rep.setEnabled(1)
            self.Sb_rp_p_rep.setEnabled(1)
            self.L_stepTimeP.setEnabled(1)
            self.Sb_stepTimeP.setEnabled(1)
            self.L_stepTimeLabP.setEnabled(1)
            self.L_rp_p_rep.setEnabled(1)
        else:
            self.Cb_rp_p_rep.setEnabled(0)
            self.Sb_rp_p_rep.setEnabled(0)
            self.L_stepTimeP.setEnabled(0)
            self.Sb_stepTimeP.setEnabled(0)
            self.L_stepTimeLabP.setEnabled(0)
            self.L_rp_p_rep.setEnabled(0)

    def repeatmode(self):
        self.Qtedit.switshformat(self.Cb_rp_p_rep.currentText())
        if self.Cb_rp_p_rep.currentText() == 'during':
            self.L_rp_p_rep.setText('h:m:s')
        if self.Cb_rp_p_rep.currentText() == 'again':
            self.L_rp_p_rep.setText('Times')

    def start(self):
        self.worker.timeStepBetweenTrack=self.stepTimePedit.gettosec()
        if self.worker.Player.statu=="pause":
            self.worker.start(self.getCurrentTrack(), self.Ch_rp_p_repeat.checkState(), self.Qtedit)
        else:
            self.worker.start_sig.emit(self.getCurrentTrack(), self.Ch_rp_p_repeat.checkState(), self.Qtedit)

    def pause(self):
        self.worker.pause()

    def stop(self):
        if self.worker.Player.statu!="stop":
            self.worker.stop()
            if self.Ch_rp_p_repeat.checkState():
                self.Qtedit.rst()
            self.setTimeProg(0)
        else:
            if self.Ch_rp_p_repeat.checkState():
                self.Qtedit.rst()
            self.setTimeProg(0)
    def expIms(self):
        self.worker.expIm_sig.emit(self.DirDialog())
    def screenDir(self):
        self.worker.screenshotDir(self.DirDialog())
    def main(self):
        #self.app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        # Window title
        
        self.swapIOmode()### IO is record/play
        self.Tw_playRecord.currentChanged.connect(self.swapIOmode)
        
        self.B_screendir.clicked.connect(self.expIms)
        self.B_screendir_P.clicked.connect(self.screenDir)
        
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.titleBar = TitleBar(self.L_WindowTiltle, self.B_close,
                                 self.B_maximize, self.B_minimize, self.frame, self)
        self.frame.layout().addWidget(self.titleBar)
        self.titleBar.setTitle("Gui Control Mime")
        # progress label
        self.L_player_time = QLabel(self.tab_2)
        
        self.L_player_time.setMinimumSize(70,0)
        self.L_player_time.setText("0 : 0 : 0 / 0:0:0")
        # self.L_player_time.setForegroundRole(QPalette.ColorRole(Qt.white))
        self.L_player_time.setAttribute(Qt.WA_TranslucentBackground)

        self.Qtedit = tmanip(self.Sb_rp_p_rep)
        self.stepTimePedit = tmanip(self.Sb_stepTimeP)
        self.stepTimePedit.switshformat("during")
        self.Sb_stepTimeP.returnPressed.connect(lambda:self.stepTimePedit.switshformat("during"))
        self.Cb_rp_p_rep.currentIndexChanged.connect(self.repeatmode)
        self.Ch_rp_p_repeat.stateChanged.connect(self.repeat)
        self.repeat()
        self.repeatmode()
        self.Sb_rp_p_rep.returnPressed.connect(lambda:self.Qtedit.switshformat(self.Cb_rp_p_rep.currentText()))
        # self.L_player_time.setTextFormat(QColor(Qt.black))
        # Thread
        self.worker = Worker()
        self.thread = QThread()
        self.worker.moveToThread(self.thread)
        self.thread.start()

        # prog bar
#        self.Pb_process=QProgressBar()
#        self.Pb_process.setObjectName("Pb_process")
#        self.Pb_process.setFixedWidth(100)
#        self.L_status=QLabel()
#        self.L_status.setObjectName("L_status")
#        self.statusBar().insertWidget(0,self.Pb_process)
#        self.statusBar().insertWidget(1,self.L_status)
#        self.Pb_process.setVisible(0)
        # Start/Stop meca
        self.Cb_screenshot_P.stateChanged.connect(lambda:self.worker.screenshotAtClick(self.Cb_screenshot_P.checkState()))
        self.Sp_imPesistancy.valueChanged.connect(self.worker.imPesistancy)
        self.Cb_screenshot.stateChanged.connect(lambda:self.worker.screenshotAtRelease(self.Cb_screenshot.checkState()))
        ### hotkey
        self.hk=hotkey()
        self.hk.set_even(self.worker.pause,["ctrl","alt","w"])
        self.hk.start()
        ###
        self.B_player_start.clicked.connect(self.start)
        self.B_player_stop.clicked.connect(self.stop)
        self.B_rec_start.clicked.connect(lambda: self.worker.recStart(
            self.getCurrentTrack(), self.Cb_relTo.checkState(), self.Cb_screenshot.checkState()))
        self.B_rec_stop.clicked.connect(self.worker.recStop)
        self.B_player_pause.clicked.connect(self.pause)
        # file management
        self.B_saveTrack.clicked.connect(self.save)
        self.B_saveAs.clicked.connect(self.saveAs)
        # signals connection
        self.setTrack_sig.connect(self.worker.setCurrentTrack)
        self.renameTrack_sig.connect(self.worker.renameCurrentTrack)
        self.removeTrack_sig.connect(self.worker.rmCurrentTrack)
        #########
        # timer
        self.play_time_sig = QTimer()
        self.play_time_sig.setSingleShot(False)
        self.rec_time_sig = QTimer()
        self.rec_time_sig.setSingleShot(False)
        self.play_time_sig.timeout.connect(lambda: self.showTime("p"))
        self.rec_time_sig.timeout.connect(lambda: self.showTime("r"))
        self.worker.setBusyFlag_sig.connect(self.set_busy_flag)
        self.worker.play_stoped_sig.connect(self.stop)
        # swap Detail button
        self.B_HS.clicked.connect(self.swapDetail)
        # track internal stack
        self.B_redo.clicked.connect(self.worker.stackNext_sig.emit)
        self.B_undo.clicked.connect(self.worker.stackPrev_sig.emit)
        # Track list
        self.Gb_trackList.setStyleSheet("QGroupBox: { flat: 1px solid gray; }")
        self.Tb_track.setAcceptDrops(True)
        self.Tb_track.dragMoveEvent = self.dragEnterEvent
        self.Tb_track.dragEnterEvent = self.dragEnterEvent
        self.Tb_track.dropEvent = self.dropEvent
        self.IDfTable = IQDataFrameWidget(self.Tb_track, flags=self.flag)
        self.IDfTable.setRaddCallback(self.add_Track)
        self.IDfTable.setDataFrame(
            DataFrame(columns=["Track name", "most used application"]), 0)
        self.IDfTable.checkAddRC(row=True, column=False, init=True)
        self.IDfTable.setRowClickedCallback(self.setTrack_sig.emit)
        self.IDfTable.setRowRenameCallback(self.renameTrack_sig.emit)
        self.IDfTable.setRemoveRowCallback(self.removeTrack_sig.emit)
        self.B_rmTrack.clicked.connect(self.IDfTable.rmCurrentRow)
        # self.IDfTable.self.worker.rmCurrentTrack
        
        self.setFixedHeight(389)
        self.setFixedWidth(978)
        self.B_logTab.clicked.connect(self.dataViewer)
        self.show()
        pos=self.Pb_playTime.pos()
        size=self.Pb_playTime.sizeHint()
        self.L_player_time.move(int(pos.x()+(size.width()/2)+70), int(pos.y()-4))
        if self.DBg:
            self.DBg.main()
        sys.exit(self.app.exec_())

    def dataViewer(self):
        ### self.standardTest()
        if (self.worker.currentTrack != "Add Track") and (self.worker.currentTrack != None):
            self.DBg.show()
            self.worker.setBusyFlag_sig.emit("currentTrack", False)

    def save(self):
        logging.info(self.worker.currentTrack+" save")
        if (self.worker.currentTrack != "Add Track") and (self.worker.currentTrack != None):
            self.worker.save_sig.emit(self.worker.currentTrack)
        else:
            self.saveAs()

    def saveAs(self):
        logging.info(self.worker.currentTrack+" saveAs")
        if (self.worker.currentTrack != "Add Track") and (self.worker.currentTrack != None):
            file = self.saveFileDialog()[0]
            if file:
                logging.info(file+" saveAs")
                self.IDfTable.QTable.item(self.IDfTable.QTable.currentRow(), 0).setText(
                    self.worker.stack[self.worker.currentTrack].filter_path(file))
                self.worker.save_sig.emit(file)

    def FileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(
            self, "QFileDialog.getOpenFileName()", "", "All Files (*);;Python Files (*.)", options=options)
        if fileName:
            return fileName
        else:
            return None

    def saveFileDialog(self, defpath=""):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        my_dir = QFileDialog.getSaveFileName(
            self, 'Save as', defpath, options=options)
        if my_dir:
            return my_dir
        else:
            return None

    def DirDialog(self, defpath=""):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        options |= QFileDialog.ShowDirsOnly
        my_dir = QFileDialog.getExistingDirectory(
            self, 'Select directory', defpath, options=options)
        if my_dir:
            return my_dir
        else:
            return None

    def setStatusTips(self, text, t=1000):
        self.statusBar().showMessage(text, t)
    def standardTest(self):
        if not "DefaultTest" in list(self.worker.stack.keys()):
            self.MultiImport([os.getcwd()+os.path.sep+"DefaultTest.ogc"])
        self.B_player_start.click()



if __name__ == "__main__":
    a = OGC(debug=True)
