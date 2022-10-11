# import cv2
# import random
# import string
# import time
# import datetime

# cap = cv2.VideoCapture(-1)
# prev_frame_time = 0
# new_frame_time = 0

# while(True):
#     ret, frame = cap.read()
#     cap.set(cv2.CAP_PROP_FPS, 5)
    
#     fps = cap.get(cv2.CAP_PROP_FPS)
#     print('set FPS:', fps)
    
#     new_frame_time = time.time()
#     fp_s = 1/(new_frame_time-prev_frame_time)
#     prev_frame_time = new_frame_time
#     print('fps get: ',fp_s)  
       
#     randm_name = (''.join(random.choices(string.ascii_letters, k=3)))
#     current_time = datetime.datetime.now()
#     # dateTime = str(current_time).replace(' ', '-')
#     cv2.imwrite("pre_processed_frame/"+str(current_time)+'_'+randm_name+'.jpg',frame)
    
import cv2
import random
import string
import time
import datetime

os.mkdir('frame')

# Open video file
video = cv2.VideoCapture('20220330_143620.mp4')


while video.isOpened():     
    ret, frame = video.read()
    fps = video.get(cv2.CAP_PROP_FPS)
    print("fps", fps)
    
    rndm_name = (''.join(random.choices(string.ascii_letters, k=3)))
    # tt = round(time.time() * 1000)
    current_time = datetime.datetime.now()
    dateTime = str(current_time).replace(' ', '_')
    cv2.imwrite("frame/"+str(dateTime)+ rndm_name +'.jpg',frame)            

