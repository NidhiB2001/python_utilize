import cv2

vidcap = cv2.VideoCapture('cut_bscSY_29-07-353.mp4')

def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC, sec*1000)
    hasFrames, image = vidcap.read()

    if hasFrames:
        cv2.imwrite("image/"+str(count)+".jpg", image)
    return hasFrames

sec = 0
frameRate = 1
count = 0

success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)

    if sec < 420:
        success = False
        success = getFrame(sec)
