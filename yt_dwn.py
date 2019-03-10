from pytube import YouTube
import moviepy.editor as mp
from bs4 import BeautifulSoup
from tinytag import TinyTag
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from mp3_tagger import MP3File
import sys
import time
import os
import requests
import threading
import unidecode as ud

from gui import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class media_file():
	def __init__(self, path, title="", ext="", album="", artist="", genre="", year="", duration=""):
		if title != "":
			self.title = title
			self.ext = ext
			self.album = album
			self.artist = artist
			self.genre = genre
			self.year = year
			self.duration = duration
			self.path = path
		else:
			self.get_data(path)

	def get_data(self, file_path):
		f = TinyTag.get(file_path)

		self.path = file_path
		self.title = file_path.split("\\")[-1]
		self.ext = self.title.split(".")[1]
		self.album = f.album if f.album != None else "_"
		self.artist = f.artist if f.artist != None else "_"
		self.year = f.album if f.year != None else "_"
		self.genre = f.album if f.genre != None else "_"
		self.duration = str(int(int(f.duration)/60))+":"+str(int(str(f.duration/60.0-int(f.duration)/60).split(".")[1][0:2]))

	def get_row(self):
		return str(self.title+","+self.album+","+self.artist+","
				   +self.genre+","+self.year+","+self.duration+","
				   +self.path+","+"mp3")

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

				tt_dur = TinyTag.get(file_path)
				duration = str(int(int(tt_dur.duration)/60))+":"+str(int(tt_dur.duration))
				
				mf = media_file(self.ofolder+"\\"+file_name+"."+self.convert,
								file_name,
								self.convert,
								"album",
								"artist",
								"genre",
								1990,
								duration)
				media_files.append(mf)
				self.emit(SIGNAL("add_row(QString)"), mf.get_row())
				
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

		self.button_openfile.clicked.connect(self.open_file)
		self.button_openfolder.clicked.connect(self.open_folder)
		
		# radio buttons
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
		self.tableWidget_files.setColumnCount(8)
		self.tableWidget_files.setHorizontalHeaderLabels(
			QString("filename,album,artist,genre,year,duration,location,file type").split(",")
		)
		header = self.tableWidget_files.horizontalHeader()
		header.resizeSection(0, 300)
		header.resizeSection(1, 150)
		header.resizeSection(2, 150)
		header.resizeSection(3, 70)
		header.resizeSection(4, 60)
		header.resizeSection(5, 60)
		header.resizeSection(6, 340)
		header.resizeSection(7, 50)
		#header.setResizeMode(2, QtGui.QHeaderView.Stretch)
		"""header.setResizeMode(1, QtGui.QHeaderView.ResizeToContents)
		header.setResizeMode(2, QtGui.QHeaderView.ResizeToContents)"""

		self.button_writetags.clicked.connect(self.write_tags)
		
		"""self.tableWidget_files.insertRow(0)
		for c in range(self.tableWidget_files.columnCount()):
			self.tableWidget_files.setItem(0, c, QTableWidgetItem("ey"+str(c)))
		self.tableWidget_files.setItem(0, 6, QTableWidgetItem("E:\ESTUDIO\PROGRAMACION\Python\YouTube-Downloader\Grito_de_terror___efeto_de_sonido.mp3"))"""

	def write_tags(self):
		print("write tags")
		new_album = self.textEdit_album.toPlainText()
		new_artist = self.textEdit_artist.toPlainText()
		new_year = self.textEdit_year.toPlainText()
		new_genre = self.textEdit_genre.toPlainText()
		new_trackn = self.textEdit_trackn.toPlainText()
		
		indexes = self.tableWidget_files.selectionModel().selectedRows()
		curr_row = self.tableWidget_files.currentItem().row()
		print(curr_row)
		
		f = EasyID3(str(self.tableWidget_files.item(curr_row, self.tableWidget_files.columnCount()-2).text()))
		print(f)
		if str(new_album) != "":
			self.tableWidget_files.setItem(curr_row, 1, QTableWidgetItem(str(new_album)))
			f["album"] = str(new_album)
		if str(new_artist) != "":
			self.tableWidget_files.setItem(curr_row, 2, QTableWidgetItem(str(new_artist)))
			f["artist"] = str(new_artist)
			f["albumartist"] = str(new_artist)
			f["composer"] = str(new_artist)
			f["performer"] = str(new_artist)
			f["author"] = str(new_artist)
			f["artistsort"] = str(new_artist)
		if str(new_year) != "":
			self.tableWidget_files.setItem(curr_row, 4, QTableWidgetItem(str(new_year)))
			f["date"] = str(new_year)
			f["originaldate"] = str(new_year)
		if str(new_genre) != "":
			f["genre"] = str(new_genre)
			self.tableWidget_files.setItem(curr_row, 3, QTableWidgetItem(str(new_genre)))
		if str(new_trackn) != "":
			f["tracknumber"] = str(new_trackn)
			# new table field

		f.save(str(self.tableWidget_files.item(curr_row, self.tableWidget_files.columnCount()-2).text()))
	
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
				self.progressbar.setMaximum(4*len(links))
				
			else:
				links = []
				links.append(str(self.textEdit_link.toPlainText()))
				self.progressbar.setMaximum(4)
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

	def open_file(self):
		selected_f = QFileDialog.getOpenFileName(self, "Select file", "", "Audio Files (*.mp3)")
		mf = media_file(str(selected_f).replace("/", "\\"))
		media_files.append(mf)		
		self.add_row_to_table(mf.get_row())
		
	def open_folder(self):
		folder = QFileDialog.getExistingDirectory(self, "Select folder")
		files = [[f for f in files if "mp3" in f] for root, dirs, files in os.walk(str(folder))][0]
		print(files)
		for f in files:
			mf = media_file(str(folder+"\\"+f))
			media_files.append(mf)
			self.add_row_to_table(mf.get_row())
			
	def print_text(self, text):
		self.progressbar.setValue(self.progressbar.value()+1)
		self.textEdit_logs.append(text)

	def add_row_to_table(self, text):
		print("new row")
		new_row_n = self.tableWidget_files.rowCount()
		self.tableWidget_files.insertRow(new_row_n)
		
		aux = text.split(",")
		for c in range(self.tableWidget_files.columnCount()):
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
	#if len(sys.argv) == 2 and sys.argv[1] == "-gui":
	media_files = []
	app = QtGui.QApplication(["YT downloader"])
	mw = MainWindow()
	mw.show()
	app.exec_()
	"""	
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
	"""
