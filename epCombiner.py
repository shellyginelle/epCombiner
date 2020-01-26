import subprocess
import os
from shutil import move
from os.path import *


#File Directory 
fileDir = os.path.dirname(os.path.abspath(__file__))    # Directory of the Module
filePath = fileDir + "\\" 
combinerFile = 'combiner.bat'
exeFile = 'mp3cat.exe'
combinerFilePath = fileDir + "\\" + combinerFile
exeFilePath = fileDir + "\\" + exeFile
audioFolderPath = fileDir + "\\audio\\"


showName = "anohana"

audioFiles = os.listdir(audioFolderPath)

# print (audioFiles)

currentEpisode = 1

for audioFile in audioFiles:
    currentEpisodeString = str(currentEpisode).rjust(2, "0") if currentEpisode < 10 else str(currentEpisode)    
    if showName+"_"+currentEpisodeString in audioFile :
        print('found')
        # move to main folder
        move(audioFolderPath+audioFile, filePath)  
    else:
        completedEpisodeFilePath = filePath+showName+currentEpisodeString +".mp3"       
        # combine mp3 
        subprocess.call(combinerFilePath)
        # rename completed file 
        os.rename(filePath+'combined.mp3',completedEpisodeFilePath)
        # move to a completed folder 
        move(completedEpisodeFilePath, fileDir+"\\completed\\")
        # increment counter
        currentEpisode = currentEpisode+1
        print(currentEpisode)
        # move current audiofile to main folder
        move(audioFolderPath+audioFile, filePath) 

# final run

currentEpisodeString = str(currentEpisode).rjust(2, "0") if currentEpisode < 10 else str(currentEpisode)    

completedEpisodeFilePath = filePath+showName+currentEpisodeString +".mp3"       
# combine mp3 
subprocess.call(combinerFilePath)
# rename completed file 
os.rename(filePath+'combined.mp3',completedEpisodeFilePath)
# move to a completed folder 
move(completedEpisodeFilePath, fileDir+"\\completed\\")