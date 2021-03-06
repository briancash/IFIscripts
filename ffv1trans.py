#!/usr/bin/env python

import subprocess
import sys
import os
import pdb
from Tkinter import *
import tkFileDialog
root = Tk()

# Create file-open dialog.
root.update()

filename = tkFileDialog.askopenfilename(parent=root)

output = filename + 'transcoded.mov'
inputxml = filename + '.xml'
outputxml = output + '.xml'

# Transcode video file writing frame md5 and output appropriately
cmd_list = ['ffmpeg',
        '-i',filename, 
        '-c:v']

codec = raw_input("Pick a codec: (1) ProRes, (2) v210 or (3) h264 ")
if codec== "1":
    cmd_list += ['prores', '-c:a', 'copy', output]  
        
elif codec == "2":
    cmd_list += ['v210', '-c:a', 'copy', output]

elif codec == "3":
    cmd_list += ['libx264', '-pix_fmt', 'yuv420p', '-c:a', 'libfaac', output] 

subprocess.call(cmd_list)    
      
# Write metadata for original video file - with open will auto close the file.
def make_mediainfo(xmlfilename, xmlvariable, inputfilename):
  with open(xmlfilename, "w+") as fo:
  	xmlvariable = subprocess.check_output(['mediainfo',
  						'-f',
  						'--language=raw', # Use verbose output.
  						'--output=XML',
  						inputfilename])       #input filename
  	fo.write(xmlvariable)
    
make_mediainfo(inputxml,'mediaxmlinput',filename)
make_mediainfo(outputxml,'mediaxmloutput',output)
	

