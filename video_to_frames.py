#!/usr/bin/env python3
import cv2
import numpy as np
from os import path


#get file path for desired video and where to save frames locally
cap = cv2.VideoCapture('./test.mp4') # default fps: 30

path_to_save = './frames'

current_frame = 0

while(True):

    #capture each frame
    ret, frame = cap.read()

    #stop loop when video ends
    if not ret:
        break

    # Save frame as a jpg file
    name = 'frame' + str(current_frame) + '.png'
    
    print ('Creating: ' + name)
    cv2.imwrite(path.join(path_to_save, name), frame)

    #keep track of how many images you end up with
    current_frame += 1


#release capture 
cap.release()
cv2.destroyAllWindows()

print('done')
