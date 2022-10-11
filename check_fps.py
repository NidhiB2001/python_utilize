import numpy as np
import cv2
import random
import string
import time
cap = cv2.VideoCapture(0)
prev_frame_time = 0
new_frame_time = 0
while(True):
    ret, frame = cap.read()
    
    new_frame_time = time.time()
    fps = 1/(new_frame_time-prev_frame_time)
    prev_frame_time = new_frame_time
    print(fps)
    rndm_name = (''.join(random.choices(string.ascii_letters, k=3)))
    cv2.imwrite("2min_frames/"+rndm_name+'.jpg',frame)
    
cap.release()