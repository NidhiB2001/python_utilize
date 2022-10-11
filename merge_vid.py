from moviepy.editor import VideoFileClip, concatenate_videoclips

#we use VideoFileClip() class create two video object, then we will merge them.
video_1 = VideoFileClip("vid2_26-08-22.avi")
video_2 = VideoFileClip("video.avi")

#Merge videos with concatenate_videoclips()
final_video= concatenate_videoclips([video_1, video_2])

final_video.write_videofile("final_video.mp4")
print('DONE Merge videos')