from qtDataframe import IQDataFrameWidget
from PyQt5.QtWidgets import QApplication, QMainWindow
import os, sys, logging, qdarkstyle
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QThread
from Track import Track
gen = 0
if __name__ == '__main__':
    if gen:
        os.system("pyuic5 -x PandasViewer\\PV.ui -o PandasViewer\\PV_ui.py")
import PandasViewer.PV_ui as PV_ui

class DFV(QMainWindow, PV_ui.Ui_MainWindow):### G interface
    def __init__(self, parent=None):
        super(DFV, self).__init__(parent)
    def main(self):
        self.setupUi(self)
        self.IDF = IQDataFrameWidget(self.tableWidget,True,True)
        self.IDF.setprogCallBack(self.PBset.setValue)
        self.DF = None
    def setMe(self,DF):
        if not self.DF or DF != self.DF:
            self.IDF.setDataFrame(DF,0)
            self.DF = DF

if __name__=="__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    dv=DFV()
    data = Track("F:\\gui_control_mime\\Testcylinder_extration_crash.ogc")
    print(data)
    dv.main()
    dv.show()
    dv.setMe(data)
    sys.exit(app.exec_())