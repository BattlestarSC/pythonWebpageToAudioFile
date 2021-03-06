import tkinter
import pyttsx3
import requests
from bs4 import BeautifulSoup
from breadability.readable import Article
import os

def audioCreationWrapper(filenameWidget, urlWidget, speedWidget, statusWidget):
	fname = str(filenameWidget.get())
	url = str(urlWidget.get())

	# make sure url and filename is valid
	if url is "" or url is None:
		statusWidget.config(text="Need a valid URL")
		return
	if fname == "" or fname is None:
		statusWidget.config(text="Need a valid output filename")
		return

	speed = speedWidget.get()
	if not speed.isnumeric():
		statusWidget.config(text="Speed must be a valid number (decimals will be truncated)")
		return
	elif speed is "":
		speed = 200
	else:
		speed = int(speed)

	# run command
	output = createAudioFile(fname,
		url,
		speed)

	# update status
	statusWidget.config(text=output)

def createAudioFile(filename : str, url : str, speed : int = 200):

	# check that the url is valid
	try:
		response = requests.get(url)
		if response.status_code is not 200:
			return "Unable to get page " + url
	except:
		return "Unable to get page " + url 

	# now actually get the response
	response = requests.get(url)

	# fix filename if needed for pyttsx3
	if len(filename) < 5:
		filename = filename + ".mp3"
	elif filename[-4] is not ".mp3":
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
	engine.save_to_file(text, filename)
    # run
	engine.runAndWait()
	engine.stop()

    # return to make sure it was completed
	return "Wrote audio to " + filename

# top/root level widget
top = tkinter.Tk()

# banner widget
bannerLabel = tkinter.Label(top, text="Web Article to MP3", font='Helvetica 18 bold')

# main settings frame
mainFrame = tkinter.Frame(top)
# url frame
urlBox = tkinter.Frame(mainFrame)
# url label
urlLabel = tkinter.Label(urlBox, text="Article url")
# url entry
urlEntry = tkinter.Entry(urlBox)
# grid pack
urlLabel.grid(row=0,
	column=0,
	sticky='w',
	pady=2)
urlEntry.grid(row=0,
	column=1,
	pady=2)

# the filename entry stuff
fileBox = tkinter.Frame(mainFrame)
# file label
fileLabel = tkinter.Label(fileBox, text="Output filename")
# file entry
fileEntry = tkinter.Entry(fileBox)
# grid pack
fileLabel.grid(row=0,
	column=0,
	sticky='w',
	pady=2)
fileEntry.grid(row=0,
	column=1,
	pady=2)

# the read speed entry boxes
# the filename entry stuff
speedBox = tkinter.Frame(mainFrame)
# speed label
speedLabel = tkinter.Label(speedBox, text="Read speed (words/minute)")
# url entry
speedEntry = tkinter.Entry(speedBox)
# grid pack
speedLabel.grid(row=0,
	column=0,
	sticky='w',
	pady=2)
speedEntry.grid(row=0,
	column=1,
	pady=2)

# Status/output box (used for failure/completion outputs)
statusFrame = tkinter.Frame(top)
statsText = tkinter.Label(statusFrame,
	text="Status: ")
statsLabel = tkinter.Label(statusFrame,
	text="Waiting")
statsText.grid(row=0,
	column=0,
	sticky='w',
	pady=2)
statsLabel.grid(row=0,
	column=1,
	pady=2)

# Run Button
runButton = tkinter.Button(top,
	text="Run",
	command= lambda: audioCreationWrapper(fileEntry, urlEntry, speedEntry, statsLabel))

# pack main shit
urlBox.grid(row=0,
	column=0,
	pady=2)
fileBox.grid(row=1,
	column=0,
	pady=2)
speedBox.grid(row=2,
	column=0,
	pady=2)

# packing party
bannerLabel.pack(fill="y",
	expand=True)
# pack the frames
mainFrame.pack(fill="both",
	expand=True)
#pack the output area
statusFrame.pack(fill="y",
	expand=True)
# pack the button 
runButton.pack(fill="y",
	expand=True)
# run the main graphics loop
top.mainloop()
