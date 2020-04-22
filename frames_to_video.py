#!/usr/bin/env python3
import cv2
import numpy as np
from os import listdir
from os.path import join, isfile

path = "./frames"

frames = []

# ignore .DS_Store
files = [f for f in listdir(path) if not f.startswith('.')]

# sort files in correct order
files.sort(key=lambda x: int(x[5:-4])) # x[5:-4] is the number
# print(files)

for f in files:
    filename = join(path, f)

    # reading each file
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)

    # append img to frames array
    frames.append(img)

fps = 30
output = cv2.VideoWriter('video.mp4', cv2.VideoWriter_fourcc('m','p','4','v'), fps, size)

# writting image to video
for img in frames:
    output.write(img)

output.release()