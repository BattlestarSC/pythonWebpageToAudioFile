import tkinter
import pyttsx3
import requests
from bs4 import BeautifulSoup
from breadability.readable import Article
import os


def createAudioFile(filename : str, url : str, speed : int = 200):

	# make sure url and filename is valid
	if url == None:
		return "Need URL"
	if filename == None:
		return "Need filename"

	# check that the url is valid
	response = requests.get(url)
	if response.status_code is not 200:
		return "Unable to get page " + url

	# fix filename if needed for pyttsx3
	if len(filename) < 5:
		filename = filename + ".mp3"
	elif ".mp3" is not in filename[-4]:
		filename = filename + ".mp3"

	# check that the filename/location is valid
	# This is really not the pythonic solution, HOWEVER
	# pyttsx3 seems to provide NO error checking or anything
	directory = os.path.abspath(os.path.dirname(filename))
	if not os.access(directory, os.W_OK):
		return "Unable to write to directory/file"

	# check for existance	
	if os.path.exists(filename):
		return "File already exists"

	# find the important stuff with readability
	doc = Article(response.content, url=url)

	# isolate text with soup
	soup = BeautifulSoup(doc.readable)
	text = soup.text

	# init speech engine
    engine = pyttsx3.init()
    # set speed
    engine.setProperty('rate', speed)
    # write to the file location
    engine.write_to_file(text, filename)
    # run
    engine.runAndWait()
    engine.stop()

    # return to make sure it was completed
    return "Wrote audio to " + filename

# top/root level widget
top = tkinter.Tk()



# run the main graphics loop
top.mainloop()