from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import glob,os
import time
import subprocess
import shutil


g_login = GoogleAuth()
g_login.LocalWebserverAuth()
drive = GoogleDrive(g_login)

subprocess.Popen("python store_video.py rtsp://airpix:airpix_123@192.168.0.228:554/HighResolutionVideo 1", shell=True)
subprocess.Popen("python store_video.py rtsp://airpix:airpix_123@192.168.0.228:554/HighResolutionVideo 2", shell=True)

os.chdir("saved")
destination = "../sent"
while(True):
    for file in glob.glob("*.avi"):
        with open(file, encoding = "ISO-8859-1") as f:
            fn = os.path.basename(f.name)
            file_drive = drive.CreateFile({ fn : fn })  
            file_drive.SetContentString(f.read()) 
            file_drive.Upload()
            shutil.move(fn,destination)
            print ( str(fn) + " fils have been uploaded")        


print ("Code stoped")
