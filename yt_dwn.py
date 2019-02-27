from pytube import YouTube
import moviepy.editor as mp
from bs4 import BeautifulSoup
from tinytag import TinyTag
import sys
import time
import os
import requests
import threading
import unidecode as ud

from gui import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *


"""def dl_video(link, ofolder):
	print("downloading video with link: \n"+str(link))
	#mw.textEdit_logs.append("downloading video with link: \n"+str(video.get("href")))
	YouTube(link).streams.first().download(ofolder)
	print("done!")
	#mw.textEdit_logs.append("done")
				
def dl_playlist(link, ofolder):
	html_page = requests.get(link)
	soup = BeautifulSoup(html_page.text, "html.parser")
	res = soup.find_all("a", {"class":"pl-video-title-link"})

	print(str(len(res))+" videos in playlist "+str(link))
	mw.textEdit_logs.append(str(len(res))+" videos in playlist "+str(link))
	for video in res:
		print("downloading video with link: \n"+str(video.get("href")))
		#mw.textEdit_logs.append("downloading video with link: \n"+str(video.get("href")))
		YouTube("https://www.youtube.com/"+video.get("href")).streams.first().download(ofolder)
		print("done!")
		#mw.textEdit_logs.append("done")"""

class media_file():
	def __init__(self, title, ext, album, artist, year, duration, path):
		self.title = title
		self.ext = ext
		self.album = album
		self.artist = artist
		self.year = year
		self.duration = duration
		self.path = path

class mwThread(QThread):
	paths = []

	def __init__(self, links, folder, convert):
		QThread.__init__(self)
		self.links = links
		self.ofolder = folder
		self.convert = convert

	def __del__(self):
		self.wait()

	def run(self):
		for link in self.links:
			print("Downloading video with link: \n"+str(link))
			file_name = ud.unidecode(YouTube(link).title.replace(" ", "_").replace(".", "-"))
			file_path = ud.unidecode(self.ofolder+"\\"+file_name+".mp4")
			print(YouTube(link).title)
			print(self.ofolder+"\\"+file_name+".mp4")
			self.emit(SIGNAL("print_text(QString)"), "Downloading video with link: \n"+str(link))
			self.emit(SIGNAL("print_text(QString)"), str(YouTube(link).title))
			YouTube(link).streams.filter(file_extension='mp4').first().download(self.ofolder, filename=file_name)
			
			if self.convert != "none":
				self.emit(SIGNAL("print_text(QString)"), "converting to ."+self.convert)
				clip = mp.VideoFileClip(file_path)
				print(ud.unidecode(file_name)+"."+self.convert)
				clip.audio.write_audiofile(self.ofolder+"\\"+file_name+"."+self.convert)

				tags = TinyTag.get(file_path)
				duration = str(int(int(tags.duration)/60))+":"+str(int(tags.duration))
				mf = media_file(file_name,
								self.convert,
								"album",
								"artist",
								1990,
								str(int(int(tags.duration)/60))+":"+str(round(int(tags.duration), 2)),
								file_path)
				media_files.append(mf)
				self.emit(SIGNAL("add_row(QString)"),str(mf.title)+","
													+str(mf.album)+","
													+str(mf.artist)+","
													+str(mf.year)+","
													+str(mf.duration)+","
													+str(mf.path)
				)
				
				clip.close()
				os.remove(file_path)
			else:
				self.emit(SIGNAL("print_text(QString)"), "...")
				
			print("Done!\n")
			self.emit(SIGNAL("download_finished"), "done!\n")

			self.paths.append(file_path)
			
class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
	playlist = False
	downloading = False
	convert = False
	
	def __init__(self, *args, **kwargs):
		QtGui.QMainWindow.__init__(self, *args, **kwargs)
		self.setupUi(self)

		self.button_search.clicked.connect(self.search_folder)
		self.button_download.clicked.connect(self.download)

		videotype_group = QtGui.QButtonGroup(self)
		self.rbutton_video.toggled.connect(lambda: self.rbutton_changed("video"))
		self.rbutton_video.setChecked(True)
		self.rbutton_playlist.toggled.connect(lambda: self.rbutton_changed("playlist"))
		videotype_group.addButton(self.rbutton_video)
		videotype_group.addButton(self.rbutton_playlist)
				
		format_group = QtGui.QButtonGroup(self)
		self.rbutton_mp4.toggled.connect(lambda: self.rbutton_changed("mp4"))
		self.rbutton_mp4.setChecked(True)
		self.rbutton_mp3.toggled.connect(lambda: self.rbutton_changed("mp3"))
		self.rbutton_wav.toggled.connect(lambda: self.rbutton_changed("wav"))
		format_group.addButton(self.rbutton_mp4)
		format_group.addButton(self.rbutton_mp3)
		format_group.addButton(self.rbutton_wav)

		# table
		#self.tableWidget_files.setRowCount(0)
		self.tableWidget_files.setColumnCount(6)
		self.tableWidget_files.setHorizontalHeaderLabels(
			QString("title,album,artist,year,duration,location").split(",")
		)
		header = self.tableWidget_files.horizontalHeader()
		header.resizeSection(0, 340)
		header.resizeSection(1, 150)
		header.resizeSection(2, 150)
		header.resizeSection(3, 60)
		header.resizeSection(4, 60)
		header.resizeSection(5, 340)
		#header.setResizeMode(2, QtGui.QHeaderView.Stretch)
		"""header.setResizeMode(1, QtGui.QHeaderView.ResizeToContents)
		header.setResizeMode(2, QtGui.QHeaderView.ResizeToContents)"""

		self.button_chalbum.clicked.connect(self.change_album)
		
		self.tableWidget_files.insertRow(0)
		for c in range(5):
			self.tableWidget_files.setItem(0, c, QTableWidgetItem("ey"+str(c)))


	def change_album(self):
		print("change album")
		indexes = self.tableWidget_files.selectionModel().selectedRows()
		for index in sorted(indexes):
			print(index.row())
			for field in range(self.tableWidget_files.columnCount()):
				print(self.tableWidget_files.item(index.row(), field).text())
	
	def search_folder(self):
		folder = QFileDialog.getExistingDirectory(self, "Output Folder")
		print(folder)
		self.textEdit_folder.setText(folder)

	def rbutton_changed(self, typ):
		if typ == "playlist":
			self.playlist = True
		elif typ == "video":
			self.playlist = False
		elif typ == "mp4":
			self.convert = "none"
		elif typ == "mp3":
			self.convert = "mp3"
		else:
			self.convert = "wav"
			
	def download(self):
		if self.textEdit_folder.toPlainText() != "" and self.textEdit_link.toPlainText() != "":
			if self.playlist:					
				#dl_playlist(str(self.textEdit_link.toPlainText()), str(self.textEdit_folder.toPlainText()))
				links = self.get_playlist_links(str(self.textEdit_link.toPlainText()))
				self.progressbar.setMaximum(3*len(links))
				
			else:
				links = []
				links.append(str(self.textEdit_link.toPlainText()))
				self.progressbar.setMaximum(3)
				#dl_video(str(self.textEdit_link.toPlainText()), str(self.textEdit_folder.toPlainText()))
				time.sleep(.5)
				#self.progressbar.setValue(100)
				
			self.mw_thread = mwThread(links,
									  str(self.textEdit_folder.toPlainText()),
									  self.convert)
			self.connect(self.mw_thread, SIGNAL("print_text(QString)"), self.print_text)
			self.connect(self.mw_thread, SIGNAL("add_row(QString)"), self.add_row_to_table)
			self.connect(self.mw_thread, SIGNAL("finished()"), self.download_finished)
			self.mw_thread.start()

	def get_playlist_links(self, plink):
		html_page = requests.get(plink)
		soup = BeautifulSoup(html_page.text, "html.parser")
		res = soup.find_all("a", {"class":"pl-video-title-link"})
		for c in range(len(res)):
			res[c] = "https://www.youtube.com/"+res[c].get("href")
			
		return res

	def print_text(self, text):
		self.progressbar.setValue(self.progressbar.value()+1)
		self.textEdit_logs.append(text)

	def add_row_to_table(self, text):
		print("new row")
		new_row_n = self.tableWidget_files.rowCount()
		self.tableWidget_files.insertRow(new_row_n)
		
		aux = text.split(",")
		for c in range(new_row_n):
			self.tableWidget_files.setItem(new_row_n, c, QTableWidgetItem(aux[c]))
	
	def download_finished(self):
		self.mw_thread.exit()
		self.progressbar.setValue(100)
		if self.playlist:
			self.textEdit_logs.append("\nplaylist download finished!\n")
		QtGui.QMessageBox.information(self, "Done!", "Download finished")
		self.progressbar.setValue(0)
				
	def keyPressEvent(self, event):
		if event.key() == QtCore.Qt.Key_Q:
			self.close()
			sys.exit()

		
if __name__ == "__main__":
	"""
	url = "https://www.youtube.com/watch?v=FckQc1Fr5jI"
	playlist = "https://www.youtube.com/playlist?list=PL5IVLTK9PtksBYBQZOPd_39avcDTknAMU"
	path_to_save = "E:\ESTUDIO\PROGRAMACION\Python\yt_dwn"
	"""

	"""app = QtGui.QApplication(sys.argv)
	mw = MainWindow()
	mw.show()
	app.exec_()"""
	
	if len(sys.argv) == 2 and sys.argv[1] == "-gui":
		media_files = []
		app = QtGui.QApplication(["YT downloader"])
		mw = MainWindow()
		mw.show()
		app.exec_()
		
	elif len(sys.argv) != 5 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
		print("way to use: ")
		print("CONSOLE mode: python yt_dnw.py [-v|--video | -p|--playlist] url -l|--location path_where_to_save")
		print("GUI mode: python yt_dnw.py -gui")
		
	else:
		if "-l" in sys.argv or "--location" in sys.argv:
			path_to_save = str(sys.argv[4])
			if not os.path.exists(path_to_save) or not os.path.isdir(path_to_save):
				print("given directory not valid")
				sys.exit()
				
			if sys.argv[1] == "-p" or sys.argv[1] == "--playlist":
				# we have a playlist link
				playlist = str(sys.argv[2])
				html_page = requests.get(playlist)
				soup = BeautifulSoup(html_page.text, "html.parser")
				res = soup.find_all("a", {"class":"pl-video-title-link"})

				print(str(len(res))+" videos in playlist "+str(playlist))
				for link in res:
					print("downloading video with link: \n"+str(link.get("href")))
					YouTube("https://www.youtube.com/"+link.get("href")).streams.first().download(path_to_save)

			elif sys.argv[1] == "-v" or sys.argv[1] == "--video":
				# we have a single video link
				video_url = str(sys.argv[2])
				print("downloading video with link: \n"+str(video_url))
				YouTube(video_url).streams.first().download(path_to_save)

		else:
			print("you need to specify a path to save your download/s (-l|--location path_where_to_save)")
			sys.exit()
