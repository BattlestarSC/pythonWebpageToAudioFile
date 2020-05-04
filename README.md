# pythonWebpageToAudioFile

## Install/usage

You need python 3.x installed. 

There are a few required python libraries so...
```python -m pip install requests tkinter pyttsx3 beautifulsoup4 git+git://github.com/bookieio/breadability.git```

Run using `python runtime.py`

## GUI usage

The program expects a valid and complete http(s)://.... url from which it will extract an article using the readability algorithm to avoid ads, nav components, and other bullshit. 

The program also expects an output filename/path that doesn't exist but can be written to. This is where the output file will be placed, as a mp3 file.

The read speed is best left around 200, but can be played with to speed up the recording. 

## Motivation/inspiration

Inspiration: none (just like anyone else whom considers themselves a programmer)

Motivation: Like many, I spend a significant portion of my life in transit, or in other positions where I can listen but not read. This ranges from wanting to not trip 12 times while walking down the street to avoiding the strange tendency where reading a wiki while driving always seems to make my vehicle flash blue and red. 

This program is designed to convert anything I'd like to read into a mp3 file I can listen to while driving. However, unlike most Text-To-Speech tools, it mostly manages to avoid a 5 minute lecture on site navigation and the standard half an hour of ads being read. 