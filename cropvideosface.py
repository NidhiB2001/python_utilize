import time
import moviepy.editor as mpy
from moviepy.video.fx.all import crop

start = time.time()

clip = mpy.VideoFileClip("cut_bscSY_29-07-353.mp4")
(w, h) = clip.size

# 109 309 153 173      
cropped_clip = crop(clip, width=220, height=250, x_center=185, y_center=380)
cropped_clip.write_videofile('crop.mp4')

end = time.time()
print("time taken", (end-start))

###########Equations#############
# x_center = height/2 + x1
# y_center = width/2 + y1