# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OGC_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(978, 389)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(99999, 99999))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setAcceptDrops(False)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.Gb_trackList = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Gb_trackList.sizePolicy().hasHeightForWidth())
        self.Gb_trackList.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        self.Gb_trackList.setFont(font)
        self.Gb_trackList.setFlat(True)
        self.Gb_trackList.setObjectName("Gb_trackList")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.Gb_trackList)
        self.gridLayout_4.setContentsMargins(1, 8, 8, 4)
        self.gridLayout_4.setHorizontalSpacing(1)
        self.gridLayout_4.setVerticalSpacing(2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.B_rmTrack = QtWidgets.QToolButton(self.Gb_trackList)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icon/moins.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.B_rmTrack.setIcon(icon)
        self.B_rmTrack.setObjectName("B_rmTrack")
        self.gridLayout_4.addWidget(self.B_rmTrack, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 3, 0, 1, 1)
        self.Tb_track = QtWidgets.QTableWidget(self.Gb_trackList)
        self.Tb_track.setMinimumSize(QtCore.QSize(0, 100))
        self.Tb_track.setAcceptDrops(True)
        self.Tb_track.setFrameShape(QtWidgets.QFrame.Panel)
        self.Tb_track.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Tb_track.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.Tb_track.setAlternatingRowColors(True)
        self.Tb_track.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.Tb_track.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.Tb_track.setObjectName("Tb_track")
        self.Tb_track.setColumnCount(0)
        self.Tb_track.setRowCount(0)
        self.Tb_track.horizontalHeader().setSortIndicatorShown(True)
        self.Tb_track.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_4.addWidget(self.Tb_track, 0, 2, 5, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.B_saveTrack = QtWidgets.QToolButton(self.Gb_trackList)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/icon/saveket.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.B_saveTrack.setIcon(icon1)
        self.B_saveTrack.setObjectName("B_saveTrack")
        self.horizontalLayout.addWidget(self.B_saveTrack)
        self.gridLayout_4.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.B_saveAs = QtWidgets.QToolButton(self.Gb_trackList)
        self.B_saveAs.setMaximumSize(QtCore.QSize(9999, 9999))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/icon/saveAsket_notsuperposed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.B_saveAs.setIcon(icon2)
        self.B_saveAs.setIconSize(QtCore.QSize(20, 20))
        self.B_saveAs.setObjectName("B_saveAs")
        self.gridLayout_4.addWidget(self.B_saveAs, 2, 0, 1, 1)
        self.gridLayout_8.addWidget(self.Gb_trackList, 2, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame.setMouseTracking(True)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setHorizontalSpacing(0)
        self.gridLayout_6.setVerticalSpacing(1)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.B_maximize = QtWidgets.QToolButton(self.frame)
        self.B_maximize.setMaximumSize(QtCore.QSize(30, 30))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/icon/wintbar/max.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.B_maximize.setIcon(icon3)
        self.B_maximize.setIconSize(QtCore.QSize(30, 30))
        self.B_maximize.setObjectName("B_maximize")
        self.gridLayout_6.addWidget(self.B_maximize, 0, 5, 1, 1)
        self.B_close = QtWidgets.QToolButton(self.frame)
        self.B_close.setMaximumSize(QtCore.QSize(30, 30))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/icon/wintbar/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.B_close.setIcon(icon4)
        self.B_close.setIconSize(QtCore.QSize(30, 30))
        self.B_close.setObjectName("B_close")
        self.gridLayout_6.addWidget(self.B_close, 0, 6, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMaximumSize(QtCore.QSize(20, 20))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/icon/whitemouselitle.ico"))
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 3, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_6.addItem(spacerItem1, 1, 0, 1, 7)
        self.L_WindowTiltle = QtWidgets.QLabel(self.frame)
        self.L_WindowTiltle.setIndent(5)
        self.L_WindowTiltle.setObjectName("L_WindowTiltle")
        self.gridLayout_6.addWidget(self.L_WindowTiltle, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem2, 0, 3, 1, 1)
        self.B_minimize = QtWidgets.QToolButton(self.frame)
        self.B_minimize.setMaximumSize(QtCore.QSize(30, 30))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/icon/wintbar/minimizeToTaskBar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.B_minimize.setIcon(icon5)
        self.B_minimize.setIconSize(QtCore.QSize(30, 30))
        self.B_minimize.setObjectName("B_minimize")
        self.gridLayout_6.addWidget(self.B_minimize, 0, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(7, 14, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem3, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.frame, 0, 0, 1, 2)
        self.W_Edit = QtWidgets.QWidget(self.centralwidget)
        self.W_Edit.setObjectName("W_Edit")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.W_Edit)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Tb_edit = QtWidgets.QTabWidget(self.W_Edit)
        self.Tb_edit.setObjectName("Tb_edit")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_7.setContentsMargins(-1, 4, -1, -1)
        self.gridLayout_7.setHorizontalSpacing(1)
        self.gridLayout_7.setVerticalSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.W_play = QtWidgets.QWidget(self.tab_3)
        self.W_play.setEnabled(True)
        self.W_play.setObjectName("W_play")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.W_play)
        self.gridLayout_10.setContentsMargins(-1, 1, -1, -1)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.Cb_screenshot_P = QtWidgets.QCheckBox(self.W_play)
        self.Cb_screenshot_P.setEnabled(True)
        self.Cb_screenshot_P.setObjectName("Cb_screenshot_P")
        self.gridLayout_10.addWidget(self.Cb_screenshot_P, 2, 0, 1, 1)
        self.B_screendir_P = QtWidgets.QToolButton(self.W_play)
        self.B_screendir_P.setEnabled(True)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/newPrefix/icon/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.B_screendir_P.setIcon(icon6)
        self.B_screendir_P.setObjectName("B_screendir_P")
        self.gridLayout_10.addWidget(self.B_screendir_P, 2, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem4, 2, 3, 1, 1)
        self.Sp_imPesistancy = QtWidgets.QSpinBox(self.W_play)
        self.Sp_imPesistancy.setEnabled(True)
        self.Sp_imPesistancy.setMaximum(9999)
        self.Sp_imPesistancy.setSingleStep(1)
        self.Sp_imPesistancy.setProperty("value", 50)
        self.Sp_imPesistancy.setObjectName("Sp_imPesistancy")
        self.gridLayout_10.addWidget(self.Sp_imPesistancy, 3, 1, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.W_play)
        self.label_2.setEnabled(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout_10.addWidget(self.label_2, 3, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Ch_rp_p_repeat = QtWidgets.QCheckBox(self.W_play)
        self.Ch_rp_p_repeat.setEnabled(True)
        self.Ch_rp_p_repeat.setObjectName("Ch_rp_p_repeat")
        self.horizontalLayout_4.addWidget(self.Ch_rp_p_repeat)
        self.Cb_rp_p_rep = QtWidgets.QComboBox(self.W_play)
        self.Cb_rp_p_rep.setEnabled(True)
        self.Cb_rp_p_rep.setMinimumSize(QtCore.QSize(50, 0))
        self.Cb_rp_p_rep.setDuplicatesEnabled(False)
        self.Cb_rp_p_rep.setFrame(False)
        self.Cb_rp_p_rep.setObjectName("Cb_rp_p_rep")
        self.Cb_rp_p_rep.addItem("")
        self.Cb_rp_p_rep.addItem("")
        self.horizontalLayout_4.addWidget(self.Cb_rp_p_rep)
        self.Sb_rp_p_rep = QtWidgets.QLineEdit(self.W_play)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Sb_rp_p_rep.sizePolicy().hasHeightForWidth())
        self.Sb_rp_p_rep.setSizePolicy(sizePolicy)
        self.Sb_rp_p_rep.setMinimumSize(QtCore.QSize(0, 0))
        self.Sb_rp_p_rep.setMaximumSize(QtCore.QSize(70, 16777215))
        self.Sb_rp_p_rep.setBaseSize(QtCore.QSize(0, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(224, 228, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(224, 228, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        self.Sb_rp_p_rep.setPalette(palette)
        self.Sb_rp_p_rep.setFrame(False)
        self.Sb_rp_p_rep.setAlignment(QtCore.Qt.AlignCenter)
        self.Sb_rp_p_rep.setObjectName("Sb_rp_p_rep")
        self.horizontalLayout_4.addWidget(self.Sb_rp_p_rep)
        self.L_rp_p_rep = QtWidgets.QLabel(self.W_play)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(13)
        self.L_rp_p_rep.setFont(font)
        self.L_rp_p_rep.setObjectName("L_rp_p_rep")
        self.horizontalLayout_4.addWidget(self.L_rp_p_rep)
        self.gridLayout_10.addLayout(self.horizontalLayout_4, 0, 0, 1, 4)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.L_stepTimeP = QtWidgets.QLabel(self.W_play)
        self.L_stepTimeP.setObjectName("L_stepTimeP")
        self.gridLayout_11.addWidget(self.L_stepTimeP, 0, 1, 1, 1)
        self.L_stepTimeLabP = QtWidgets.QLabel(self.W_play)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(13)
        self.L_stepTimeLabP.setFont(font)
        self.L_stepTimeLabP.setObjectName("L_stepTimeLabP")
        self.gridLayout_11.addWidget(self.L_stepTimeLabP, 0, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem5, 0, 0, 1, 1)
        self.Sb_stepTimeP = QtWidgets.QLineEdit(self.W_play)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Sb_stepTimeP.sizePolicy().hasHeightForWidth())
        self.Sb_stepTimeP.setSizePolicy(sizePolicy)
        self.Sb_stepTimeP.setMinimumSize(QtCore.QSize(0, 0))
        self.Sb_stepTimeP.setMaximumSize(QtCore.QSize(70, 16777215))
        self.Sb_stepTimeP.setBaseSize(QtCore.QSize(0, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(224, 228, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(224, 228, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        self.Sb_stepTimeP.setPalette(palette)
        self.Sb_stepTimeP.setFrame(False)
        self.Sb_stepTimeP.setAlignment(QtCore.Qt.AlignCenter)
        self.Sb_stepTimeP.setObjectName("Sb_stepTimeP")
        self.gridLayout_11.addWidget(self.Sb_stepTimeP, 0, 2, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_11, 1, 0, 1, 4)
        self.gridLayout_7.addWidget(self.W_play, 2, 0, 1, 3)
        self.W_record = QtWidgets.QWidget(self.tab_3)
        self.W_record.setObjectName("W_record")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.W_record)
        self.gridLayout_9.setContentsMargins(-1, 1, -1, -1)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.Cb_relTo = QtWidgets.QCheckBox(self.W_record)
        self.Cb_relTo.setChecked(True)
        self.Cb_relTo.setObjectName("Cb_relTo")
        self.gridLayout_9.addWidget(self.Cb_relTo, 0, 0, 1, 2)
        self.B_screendir = QtWidgets.QToolButton(self.W_record)
        self.B_screendir.setIcon(icon6)
        self.B_screendir.setObjectName("B_screendir")
        self.gridLayout_9.addWidget(self.B_screendir, 1, 1, 1, 1)
        self.Cb_screenshot = QtWidgets.QCheckBox(self.W_record)
        self.Cb_screenshot.setObjectName("Cb_screenshot")
        self.gridLayout_9.addWidget(self.Cb_screenshot, 1, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem6, 1, 2, 1, 1)
        self.gridLayout_7.addWidget(self.W_record, 1, 0, 1, 3)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem7, 3, 0, 1, 3)
        self.B_undo = QtWidgets.QToolButton(self.tab_3)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/newPrefix/icon/undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.B_undo.setIcon(icon7)
        self.B_undo.setIconSize(QtCore.QSize(25, 25))
        self.B_undo.setObjectName("B_undo")
        self.gridLayout_7.addWidget(self.B_undo, 0, 0, 1, 1)
        self.B_redo = QtWidgets.QToolButton(self.tab_3)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/newPrefix/icon/redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.B_redo.setIcon(icon8)
        self.B_redo.setIconSize(QtCore.QSize(25, 25))
        self.B_redo.setObjectName("B_redo")
        self.gridLayout_7.addWidget(self.B_redo, 0, 1, 1, 1)
        self.Tb_edit.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.Tb_edit.addTab(self.tab_4, "")
        self.gridLayout_2.addWidget(self.Tb_edit, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.W_Edit, 1, 1, 2, 1)
        self.Tw_playRecord = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tw_playRecord.sizePolicy().hasHeightForWidth())
        self.Tw_playRecord.setSizePolicy(sizePolicy)
        self.Tw_playRecord.setMinimumSize(QtCore.QSize(0, 110))
        self.Tw_playRecord.setMaximumSize(QtCore.QSize(50000, 150))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        self.Tw_playRecord.setFont(font)
        self.Tw_playRecord.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.Tw_playRecord.setObjectName("Tw_playRecord")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.B_player_start = QtWidgets.QToolButton(self.tab_2)
        self.B_player_start.setMinimumSize(QtCore.QSize(40, 40))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/newPrefix/icon/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.B_player_start.setIcon(icon9)
        self.B_player_start.setIconSize(QtCore.QSize(30, 30))
        self.B_player_start.setObjectName("B_player_start")
        self.gridLayout_3.addWidget(self.B_player_start, 0, 0, 1, 1)
        self.B_player_pause = QtWidgets.QToolButton(self.tab_2)
        self.B_player_pause.setMinimumSize(QtCore.QSize(40, 40))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/newPrefix/icon/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.B_player_pause.setIcon(icon10)
        self.B_player_pause.setIconSize(QtCore.QSize(30, 30))
        self.B_player_pause.setObjectName("B_player_pause")
        self.gridLayout_3.addWidget(self.B_player_pause, 0, 1, 1, 1)
        self.B_player_stop = QtWidgets.QToolButton(self.tab_2)
        self.B_player_stop.setMinimumSize(QtCore.QSize(40, 40))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/newPrefix/icon/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.B_player_stop.setIcon(icon11)
        self.B_player_stop.setIconSize(QtCore.QSize(30, 30))
        self.B_player_stop.setObjectName("B_player_stop")
        self.gridLayout_3.addWidget(self.B_player_stop, 0, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Pb_playTime = QtWidgets.QProgressBar(self.tab_2)
        self.Pb_playTime.setProperty("value", 0)
        self.Pb_playTime.setTextVisible(False)
        self.Pb_playTime.setInvertedAppearance(False)
        self.Pb_playTime.setObjectName("Pb_playTime")
        self.verticalLayout.addWidget(self.Pb_playTime)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 3, 1, 1)
        self.Tw_playRecord.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(4)
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.B_rec_stop = QtWidgets.QToolButton(self.tab)
        self.B_rec_stop.setIcon(icon11)
        self.B_rec_stop.setIconSize(QtCore.QSize(30, 30))
        self.B_rec_stop.setObjectName("B_rec_stop")
        self.gridLayout.addWidget(self.B_rec_stop, 0, 1, 1, 1)
        self.L_rec_time = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        self.L_rec_time.setFont(font)
        self.L_rec_time.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.L_rec_time.setObjectName("L_rec_time")
        self.gridLayout.addWidget(self.L_rec_time, 0, 2, 1, 1)
        self.B_rec_start = QtWidgets.QToolButton(self.tab)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/newPrefix/icon/rec.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.B_rec_start.setIcon(icon12)
        self.B_rec_start.setIconSize(QtCore.QSize(30, 30))
        self.B_rec_start.setObjectName("B_rec_start")
        self.gridLayout.addWidget(self.B_rec_start, 0, 0, 1, 1)
        self.Tw_playRecord.addTab(self.tab, "")
        self.gridLayout_8.addWidget(self.Tw_playRecord, 1, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setHorizontalSpacing(3)
        self.gridLayout_5.setVerticalSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.L_status = QtWidgets.QLabel(self.centralwidget)
        self.L_status.setObjectName("L_status")
        self.gridLayout_5.addWidget(self.L_status, 0, 2, 1, 1)
        self.B_HS = QtWidgets.QToolButton(self.centralwidget)
        self.B_HS.setEnabled(True)
        self.B_HS.setMaximumSize(QtCore.QSize(40, 25))
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/newPrefix/icon/up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.B_HS.setIcon(icon13)
        self.B_HS.setIconSize(QtCore.QSize(40, 40))
        self.B_HS.setArrowType(QtCore.Qt.NoArrow)
        self.B_HS.setObjectName("B_HS")
        self.gridLayout_5.addWidget(self.B_HS, 0, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem8, 0, 1, 1, 1)
        self.B_logTab = QtWidgets.QToolButton(self.centralwidget)
        self.B_logTab.setObjectName("B_logTab")
        self.gridLayout_5.addWidget(self.B_logTab, 0, 3, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_5, 3, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Tb_edit.setCurrentIndex(0)
        self.Cb_rp_p_rep.setCurrentIndex(1)
        self.Tw_playRecord.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.B_minimize, self.B_maximize)
        MainWindow.setTabOrder(self.B_maximize, self.B_close)
        MainWindow.setTabOrder(self.B_close, self.Tw_playRecord)
        MainWindow.setTabOrder(self.Tw_playRecord, self.B_player_start)
        MainWindow.setTabOrder(self.B_player_start, self.B_player_pause)
        MainWindow.setTabOrder(self.B_player_pause, self.B_player_stop)
        MainWindow.setTabOrder(self.B_player_stop, self.B_saveTrack)
        MainWindow.setTabOrder(self.B_saveTrack, self.B_saveAs)
        MainWindow.setTabOrder(self.B_saveAs, self.B_rmTrack)
        MainWindow.setTabOrder(self.B_rmTrack, self.B_HS)
        MainWindow.setTabOrder(self.B_HS, self.B_rec_start)
        MainWindow.setTabOrder(self.B_rec_start, self.B_rec_stop)
        MainWindow.setTabOrder(self.B_rec_stop, self.Tb_track)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gui Control Mime"))
        self.Gb_trackList.setTitle(_translate("MainWindow", "Track list"))
        self.B_rmTrack.setToolTip(_translate("MainWindow", "Remove the current Track"))
        self.B_rmTrack.setText(_translate("MainWindow", "..."))
        self.Tb_track.setSortingEnabled(True)
        self.B_saveTrack.setToolTip(_translate("MainWindow", "Save"))
        self.B_saveTrack.setText(_translate("MainWindow", "..."))
        self.B_saveAs.setToolTip(_translate("MainWindow", "Save as"))
        self.B_saveAs.setText(_translate("MainWindow", "..."))
        self.B_maximize.setText(_translate("MainWindow", "..."))
        self.B_close.setText(_translate("MainWindow", "..."))
        self.L_WindowTiltle.setText(_translate("MainWindow", "Gui ControlMime"))
        self.B_minimize.setText(_translate("MainWindow", "..."))
        self.Cb_screenshot_P.setText(_translate("MainWindow", "Screenshot at clicks"))
        self.B_screendir_P.setToolTip(_translate("MainWindow", "Save screenshot\'s"))
        self.B_screendir_P.setText(_translate("MainWindow", "..."))
        self.label_2.setText(_translate("MainWindow", "Image count max:"))
        self.Ch_rp_p_repeat.setToolTip(_translate("MainWindow", "Repeat some times the current track"))
        self.Ch_rp_p_repeat.setText(_translate("MainWindow", "Loop on this track"))
        self.Cb_rp_p_rep.setItemText(0, _translate("MainWindow", "during"))
        self.Cb_rp_p_rep.setItemText(1, _translate("MainWindow", "again"))
        self.Sb_rp_p_rep.setText(_translate("MainWindow", "00:00:00"))
        self.L_rp_p_rep.setText(_translate("MainWindow", "Times"))
        self.L_stepTimeP.setText(_translate("MainWindow", "Step time between each reading:"))
        self.L_stepTimeLabP.setText(_translate("MainWindow", "H:M:S"))
        self.Sb_stepTimeP.setText(_translate("MainWindow", "00:00:00"))
        self.Cb_relTo.setText(_translate("MainWindow", "Relative to each clicked windows"))
        self.B_screendir.setToolTip(_translate("MainWindow", "Save reference (from record) screenshot\'s to a folder"))
        self.B_screendir.setText(_translate("MainWindow", "..."))
        self.Cb_screenshot.setStatusTip(_translate("MainWindow", "If screenshot points in played track"))
        self.Cb_screenshot.setText(_translate("MainWindow", "Screenshot at clicks"))
        self.B_undo.setStatusTip(_translate("MainWindow", "Undo"))
        self.B_undo.setText(_translate("MainWindow", "..."))
        self.B_redo.setStatusTip(_translate("MainWindow", "Redo"))
        self.B_redo.setText(_translate("MainWindow", "..."))
        self.Tb_edit.setTabText(self.Tb_edit.indexOf(self.tab_3), _translate("MainWindow", "Track edition"))
        self.Tb_edit.setTabText(self.Tb_edit.indexOf(self.tab_4), _translate("MainWindow", "Project edition"))
        self.B_player_start.setText(_translate("MainWindow", "..."))
        self.B_player_pause.setText(_translate("MainWindow", "..."))
        self.B_player_stop.setText(_translate("MainWindow", "..."))
        self.Tw_playRecord.setTabText(self.Tw_playRecord.indexOf(self.tab_2), _translate("MainWindow", "Play"))
        self.B_rec_stop.setText(_translate("MainWindow", "..."))
        self.L_rec_time.setText(_translate("MainWindow", "0:0:0"))
        self.B_rec_start.setText(_translate("MainWindow", "..."))
        self.Tw_playRecord.setTabText(self.Tw_playRecord.indexOf(self.tab), _translate("MainWindow", "Record"))
        self.L_status.setText(_translate("MainWindow", "Status"))
        self.B_HS.setText(_translate("MainWindow", "..."))
        self.B_logTab.setText(_translate("MainWindow", "Current Track"))

import image_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
