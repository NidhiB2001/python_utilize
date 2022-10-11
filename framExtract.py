import sys
import time
import os
import cv2
print(cv2.version)

def extractImages(pathIn, pathOut):
    count = 0
    path = pathIn.split('/')[1].split('.')[0]
    try:
        os.mkdir('data/'+path)
    except Exception as e:
        raise 
    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    success = True
    while success:
        cureent_time = round(time.time()*1000)
        print("count:::",count)
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))    
        success,image = vidcap.read()
        print ('Read a new frame: ', success)
        try:
            cv2.imwrite(pathOut+path+'/'+str(cureent_time)+''+str(round(count*10))+'.jpg', image)     
        except:
            pass
        count += 0.1

if __name__=="__main__":
    extractImages("vid_data/3rd floor _ch13_20220906090325_20220906090504.mp4", "data/")


