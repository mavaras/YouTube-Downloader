# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(419, 509)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/Mario/.designer/leap/PCRecognizer_LEAP/background.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.rbutton_video = QtGui.QRadioButton(self.centralwidget)
        self.rbutton_video.setGeometry(QtCore.QRect(30, 80, 82, 17))
        self.rbutton_video.setChecked(True)
        self.rbutton_video.setAutoExclusive(True)
        self.rbutton_video.setObjectName(_fromUtf8("rbutton_video"))
        self.rbutton_playlist = QtGui.QRadioButton(self.centralwidget)
        self.rbutton_playlist.setGeometry(QtCore.QRect(130, 80, 82, 17))
        self.rbutton_playlist.setAutoExclusive(True)
        self.rbutton_playlist.setObjectName(_fromUtf8("rbutton_playlist"))
        self.textEdit_link = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_link.setGeometry(QtCore.QRect(30, 50, 351, 21))
        self.textEdit_link.setAcceptDrops(True)
        self.textEdit_link.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_link.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_link.setObjectName(_fromUtf8("textEdit_link"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 22, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setLineWidth(1)
        self.label.setObjectName(_fromUtf8("label"))
        self.button_download = QtGui.QPushButton(self.centralwidget)
        self.button_download.setGeometry(QtCore.QRect(30, 230, 121, 23))
        self.button_download.setObjectName(_fromUtf8("button_download"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 210, 351, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.progressbar = QtGui.QProgressBar(self.centralwidget)
        self.progressbar.setGeometry(QtCore.QRect(260, 230, 121, 23))
        font = QtGui.QFont()
        font.setKerning(True)
        self.progressbar.setFont(font)
        self.progressbar.setProperty("value", 0)
        self.progressbar.setTextVisible(False)
        self.progressbar.setObjectName(_fromUtf8("progressbar"))
        self.button_search = QtGui.QPushButton(self.centralwidget)
        self.button_search.setGeometry(QtCore.QRect(310, 180, 75, 23))
        self.button_search.setObjectName(_fromUtf8("button_search"))
        self.textEdit_folder = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_folder.setEnabled(True)
        self.textEdit_folder.setGeometry(QtCore.QRect(30, 180, 261, 21))
        self.textEdit_folder.setAcceptDrops(True)
        self.textEdit_folder.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_folder.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_folder.setObjectName(_fromUtf8("textEdit_folder"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 150, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.textEdit_logs = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_logs.setEnabled(True)
        self.textEdit_logs.setGeometry(QtCore.QRect(30, 270, 351, 181))
        self.textEdit_logs.setAcceptDrops(True)
        self.textEdit_logs.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_logs.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_logs.setReadOnly(True)
        self.textEdit_logs.setObjectName(_fromUtf8("textEdit_logs"))
        self.rbutton_mp3 = QtGui.QRadioButton(self.centralwidget)
        self.rbutton_mp3.setGeometry(QtCore.QRect(130, 100, 41, 17))
        self.rbutton_mp3.setAutoExclusive(True)
        self.rbutton_mp3.setObjectName(_fromUtf8("rbutton_mp3"))
        self.rbutton_mp4 = QtGui.QRadioButton(self.centralwidget)
        self.rbutton_mp4.setGeometry(QtCore.QRect(30, 100, 41, 17))
        self.rbutton_mp4.setChecked(True)
        self.rbutton_mp4.setAutoExclusive(True)
        self.rbutton_mp4.setObjectName(_fromUtf8("rbutton_mp4"))
        self.rbutton_wav = QtGui.QRadioButton(self.centralwidget)
        self.rbutton_wav.setGeometry(QtCore.QRect(220, 100, 41, 17))
        self.rbutton_wav.setAutoExclusive(True)
        self.rbutton_wav.setObjectName(_fromUtf8("rbutton_wav"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 419, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "YouTube Downloader", None))
        self.rbutton_video.setText(_translate("MainWindow", "Single Video", None))
        self.rbutton_playlist.setText(_translate("MainWindow", "Playlist", None))
        self.label.setText(_translate("MainWindow", "Youtube link", None))
        self.button_download.setText(_translate("MainWindow", "Start Download", None))
        self.button_search.setText(_translate("MainWindow", "Search", None))
        self.label_2.setText(_translate("MainWindow", "Output Folder", None))
        self.rbutton_mp3.setText(_translate("MainWindow", "mp3", None))
        self.rbutton_mp4.setText(_translate("MainWindow", "mp4", None))
        self.rbutton_wav.setText(_translate("MainWindow", "wav", None))

