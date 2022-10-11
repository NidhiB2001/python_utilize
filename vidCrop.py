import cv2
import random
import string

vid_path = input("Enter video path -> ")
        
cam = cv2.VideoCapture(vid_path)          

imW = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
imH = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
print('im height & width ;;;;;;;;;;;;;;;',imW, imH)

scale=20

# croping values
# x,y,h,w = 700, 300, 1000, 5000                                          #700,600,5000,2500 

while cam.isOpened():     
    print("*********************************************************************************")                           
    
    ret, frame = cam.read()
    if not ret:
        break
        
    '''ZOOM video frame'''
    #prepare the crop for zoom
    centerX,centerY = int(imH/1),int(imW/1)
    radiusX,radiusY = int(scale*imH/50),int(scale*imW/50)

    minX,maxX=centerX-radiusX,centerX+radiusX
    minY,maxY=centerY-radiusY,centerY+radiusY

    zmcrop = frame[minX:maxX, minY:maxY]
    # OR
    # zmcrop = frame[y:y+h, x:x+w]
    
    hei = zmcrop.shape[0]
    wid = zmcrop.shape[1]
    print('height & width______________', hei, '&', wid)
    # print("type & zoom cropped///////////////",type(zmcrop), zmcrop)
    
    x = (''.join(random.choices(string.ascii_letters, k=3)))
    cv2.imwrite('zoom/'+x+'.jpg',zmcrop)   