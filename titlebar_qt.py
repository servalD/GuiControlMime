#########################################################
## customize Title bar
## dotpy.ir
## iraj.jelo@gmail.com
#########################################################
import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

class TitleBar(QtWidgets.QDialog):
    def __init__(self, label, close, B_max, B_min, frame, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.parent = parent
        self.minimize = B_min
        self.maximize = B_max
        self.label = label
        self.moving = False
        self.minimize.setMinimumHeight(30)
        self.minimize.setMinimumWidth(30)
        close.setMinimumHeight(30)
        close.setMinimumWidth(30)
        self.maximize.setMinimumHeight(30)
        self.maximize.setMinimumWidth(30)
        self.setMouseTracking(True)
        frame.mousePressEvent=self.fmousePressEvent
        frame.mouseMoveEvent=self.fmouseMoveEvent
        frame.mouseReleaseEvent=self.fmouseReleaseEvent
        self.setTitle("Window Title")
        self.maxNormal=False
        close.clicked.connect(self.close)
        self.minimize.clicked.connect(self.showSmall)
        self.maximize.clicked.connect(self.showMaxRestore)
    def setTitle(self, title):
        self.label.setText(title)
        self.setWindowTitle(title)
            
    def showSmall(self):
        self.parent.showMinimized()

    def showMaxRestore(self):
        if(self.maxNormal):
            self.parent.showNormal()
            self.maxNormal= False
            self.maximize.setIcon(QtGui.QIcon(':/newPrefix/icon/wintbar/max.png'))
        else:
            self.parent.showMaximized()
            self.maxNormal=  True
            self.maximize.setIcon(QtGui.QIcon(':/newPrefix/icon/wintbar/min.png'))

    def close(self):
        self.parent.close()

    def fmousePressEvent(self,event):
        if event.button() == Qt.LeftButton:
            self.moving = True
            self.offset = event.pos()

    def fmouseMoveEvent(self,event):
        if self.moving:
            self.parent.move(event.globalPos()-self.offset)

    def fmouseReleaseEvent(self,event):
        self.moving = False
class Frame(QtWidgets.QFrame):
    def __init__(self, parent=None):
        QtWidgets.QFrame.__init__(self, parent)
        if parent==None:
            self.parent = self
        else:
            self.parent = parent
        self.m_mouse_down= False
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        css = """
        QFrame{
            font:13px ;
            }
        """
        self.setStyleSheet(css)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setMouseTracking(True)
        self.m_titleBar= TitleBar(self)
        self.m_content= QtWidgets.QWidget(self)
        vbox=QtWidgets.QVBoxLayout(self)
        vbox.addWidget(self.m_titleBar)
        vbox.setContentsMargins(0, 0, 0, 0)
        vbox.setSpacing(0)
        layout=QtWidgets.QVBoxLayout()
        layout.addWidget(self.m_content)
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(0)
        vbox.addLayout(layout)
        # Allows you to access the content area of the frame
        # where widgets and layouts can be added

    def contentWidget(self):
        return self.m_content

    def titleBar(self):
        return self.m_titleBar

    def mousePressEvent(self,event):
        self.m_old_pos = event.pos()
        self.m_mouse_down = event.button()== Qt.LeftButton

    def mouseMoveEvent(self,event):
        x=event.x()
        y=event.y()

    def mouseReleaseEvent(self,event):
        m_mouse_down=False

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    box = Frame()
    box.move(60,60)
    l=QtWidgets.QVBoxLayout(box.contentWidget())
    l.setContentsMargins(0, 0, 0, 0)
    edit=QtWidgets.QLabel("""I would've did anything for you to show you how much I adored you
But it's over now, it's too late to save our loveJust promise me you'll think of me
Every time you look up in the sky and see a star 'cuz I'm  your star.""")
    l.addWidget(edit)
    box.show()
    app.exec_()
