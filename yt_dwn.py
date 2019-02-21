from pytube import YouTube
import moviepy.editor as mp
from bs4 import BeautifulSoup
import sys
import time
import os
import requests
import threading

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


class mwThread(QThread):
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
			file_name = YouTube(link).title.replace(" ", "_").replace(".", "-")
			file_path = self.ofolder+"\\"+file_name+".mp4"
			print(YouTube(link).title)
			print(self.ofolder+"\\"+file_name+".mp4")
			self.emit(SIGNAL("print_text(QString)"), "Downloading video with link: \n"+str(link))
			self.emit(SIGNAL("print_text(QString)"), str(YouTube(link).title))
			YouTube(link).streams.first().download(self.ofolder, filename=file_name)

			if self.convert:
				self.emit(SIGNAL("print_text(QString)"), "converting to .mp3")
				clip = mp.VideoFileClip(file_path)
				clip.audio.write_audiofile(file_name+".mp3")

				#os.remove(file_path)
			else:
				self.emit(SIGNAL("print_text(QString)"), "...")
				
			print("Done!\n")
			self.emit(SIGNAL("print_text(QString)"), "done!\n")
		
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
		format_group.addButton(self.rbutton_mp4)
		format_group.addButton(self.rbutton_mp3)

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
			self.convert = False
		else:
			self.convert = True
			
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
				time.sleep(1)
				#self.progressbar.setValue(100)
				
			self.mw_thread = mwThread(links, str(self.textEdit_folder.toPlainText()), self.convert)
			self.connect(self.mw_thread, SIGNAL("print_text(QString)"), self.print_text)
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

	def download_finished(self):
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
