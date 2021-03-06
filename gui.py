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
        MainWindow.resize(1046, 664)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/Mario/.designer/leap/PCRecognizer_LEAP/background.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.rbutton_video = QtGui.QRadioButton(self.centralwidget)
        self.rbutton_video.setGeometry(QtCore.QRect(30, 80, 82, 17))
        self.rbutton_video.setChecked(False)
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
        self.textEdit_logs.setGeometry(QtCore.QRect(30, 270, 351, 341))
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
        self.tableWidget_files = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget_files.setGeometry(QtCore.QRect(430, 70, 591, 381))
        self.tableWidget_files.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_files.setObjectName(_fromUtf8("tableWidget_files"))
        self.tableWidget_files.setColumnCount(0)
        self.tableWidget_files.setRowCount(0)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(396, 20, 20, 591))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.button_writetags = QtGui.QPushButton(self.centralwidget)
        self.button_writetags.setGeometry(QtCore.QRect(830, 470, 191, 141))
        self.button_writetags.setObjectName(_fromUtf8("button_writetags"))
        self.textEdit_album = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_album.setEnabled(True)
        self.textEdit_album.setGeometry(QtCore.QRect(500, 470, 301, 21))
        self.textEdit_album.setAcceptDrops(True)
        self.textEdit_album.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_album.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_album.setObjectName(_fromUtf8("textEdit_album"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(430, 470, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(430, 510, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.textEdit_artist = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_artist.setEnabled(True)
        self.textEdit_artist.setGeometry(QtCore.QRect(500, 510, 301, 21))
        self.textEdit_artist.setAcceptDrops(True)
        self.textEdit_artist.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_artist.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_artist.setObjectName(_fromUtf8("textEdit_artist"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(430, 550, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.textEdit_year = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_year.setEnabled(True)
        self.textEdit_year.setGeometry(QtCore.QRect(500, 550, 81, 21))
        self.textEdit_year.setAcceptDrops(True)
        self.textEdit_year.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_year.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_year.setObjectName(_fromUtf8("textEdit_year"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(650, 590, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.button_searchphoto = QtGui.QPushButton(self.centralwidget)
        self.button_searchphoto.setGeometry(QtCore.QRect(720, 586, 81, 23))
        self.button_searchphoto.setObjectName(_fromUtf8("button_searchphoto"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(650, 550, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.textEdit_genre = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_genre.setEnabled(True)
        self.textEdit_genre.setGeometry(QtCore.QRect(720, 550, 81, 21))
        self.textEdit_genre.setAcceptDrops(True)
        self.textEdit_genre.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_genre.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_genre.setObjectName(_fromUtf8("textEdit_genre"))
        self.button_openfile = QtGui.QPushButton(self.centralwidget)
        self.button_openfile.setGeometry(QtCore.QRect(430, 30, 91, 23))
        self.button_openfile.setObjectName(_fromUtf8("button_openfile"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(430, 590, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.textEdit_trackn = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_trackn.setEnabled(True)
        self.textEdit_trackn.setGeometry(QtCore.QRect(500, 590, 81, 21))
        self.textEdit_trackn.setAcceptDrops(True)
        self.textEdit_trackn.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_trackn.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_trackn.setObjectName(_fromUtf8("textEdit_trackn"))
        self.button_openfolder = QtGui.QPushButton(self.centralwidget)
        self.button_openfolder.setGeometry(QtCore.QRect(550, 30, 91, 23))
        self.button_openfolder.setObjectName(_fromUtf8("button_openfolder"))
        self.button_openfolder_2 = QtGui.QPushButton(self.centralwidget)
        self.button_openfolder_2.setGeometry(QtCore.QRect(950, 30, 71, 23))
        self.button_openfolder_2.setObjectName(_fromUtf8("button_openfolder_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1046, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOfficial_Site = QtGui.QAction(MainWindow)
        self.actionOfficial_Site.setObjectName(_fromUtf8("actionOfficial_Site"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuAbout.addAction(self.actionOfficial_Site)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuAbout.menuAction())

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
        self.button_writetags.setText(_translate("MainWindow", "Write tags", None))
        self.label_3.setText(_translate("MainWindow", "Album", None))
        self.label_4.setText(_translate("MainWindow", "Artist", None))
        self.label_5.setText(_translate("MainWindow", "Year", None))
        self.label_6.setText(_translate("MainWindow", "Photo", None))
        self.button_searchphoto.setText(_translate("MainWindow", "Search", None))
        self.label_7.setText(_translate("MainWindow", "Genre", None))
        self.button_openfile.setText(_translate("MainWindow", "Open File", None))
        self.label_8.setText(_translate("MainWindow", "Track nº", None))
        self.button_openfolder.setText(_translate("MainWindow", "Open Folder", None))
        self.button_openfolder_2.setText(_translate("MainWindow", "Clear", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.actionOfficial_Site.setText(_translate("MainWindow", "Official Site", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))

