#---------------------------------
# Inputs
#---------------------------------
import subprocess
import os
from shutil import move
from os.path import *

#---------------------------------
# File Directory
#---------------------------------
fileDir = os.path.dirname(os.path.abspath(__file__))    # Directory of the Module
filePath = fileDir + "\\" 
combinerFile = 'combiner.bat'
exeFile = 'mp3cat.exe'
combinerFilePath = fileDir + "\\" + combinerFile
exeFilePath = fileDir + "\\" + exeFile
audioFolderPath = fileDir + "\\audio\\"

#---------------------------------
# Variables 
#---------------------------------
showName = "anohana"
audioFiles = os.listdir(audioFolderPath)
currentEpisode = 1 

# print (audioFiles)

#---------------------------------
# Functions
#---------------------------------
def get_currentEpisodeString(currentEpisode):
    currentEpisodeString = str(currentEpisode).rjust(2, "0") if currentEpisode < 10 else str(currentEpisode)
    return currentEpisodeString

def combineAndComplete():
    completedEpisodeFilePath = filePath+showName+currentEpisodeString +".mp3"       
    # combine mp3 
    subprocess.call(combinerFilePath)
    # rename completed file 
    os.rename(filePath+'combined.mp3',completedEpisodeFilePath)
    # move to a completed folder 
    move(completedEpisodeFilePath, fileDir+"\\completed\\")

#---------------------------------
# Loop Through
#---------------------------------
for audioFile in audioFiles:
    currentEpisodeString = get_currentEpisodeString(1)    
    if showName+"_"+currentEpisodeString in audioFile :
        print('found')
        # move to main folder
        move(audioFolderPath+audioFile, filePath)  
    else:
        combineAndComplete()
        # increment counter
        currentEpisode += 1
        print(currentEpisode)
        # move current audiofile to main folder
        move(audioFolderPath+audioFile, filePath) 

# final run
currentEpisodeString = get_currentEpisodeString(1)  
combineAndComplete()