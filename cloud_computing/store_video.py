import numpy as np
import cv2
import time
import sys
from time import gmtime, strftime
import time as Time
import subprocess
import os
import shutil

video_ = sys.argv[1]
camera_number = sys.argv[2]

video_capture = cv2.VideoCapture()
video_capture.open(str(video_))
os.chdir("saving")
destination = "../saved"
print("In subprocess")
writeVideo_flag = True 

time_per_video = 10 #in sec

def initiate_out():
    global out , t,filename
    named_tuple = Time.localtime()
    time_string = time.strftime("_%m_%d_%Y_%H_%M_%S_", named_tuple)

    if writeVideo_flag:
        # Define the codec and create VideoWriter object
        w = int(video_capture.get(3))
        h = int(video_capture.get(4))
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        filename = str(camera_number) + time_string + ".avi"
        out = cv2.VideoWriter( filename , fourcc, 15, (w, h))
        t = time.time()

new_video = True
while(True):

    if(new_video):
        initiate_out()
        new_video = False
    
    else:    
        ret, frame = video_capture.read()
        #cv2.imshow('frame',frame)
        
        if((time.time() - t) > time_per_video):
            out.release()
            shutil.move(filename,destination)
            new_video = True   
        
        if writeVideo_flag:
            out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    
print("subprocess end")        
video_capture.release()
if writeVideo_flag:
    out.release()
cv2.destroyAllWindows()
