import os
##import library for work with video
import moviepy.editor

##import for show dialog to select file
from tkinter.filedialog import *

#function to open file
video = askopenfilename()



video = moviepy.editor.VideoFileClip(video)
# ext_name =os.path.basename(video)
audio = video.audio

audio.write_audiofile('extract audio!')
# audio.write_audiofile(ext_name)
print(" Completed! :)")