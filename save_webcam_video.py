import numpy as np
import cv2

cap = cv2.VideoCapture(0)

fps = cap.get(cv2.CAP_PROP_FPS)
#print(fps)
vidW = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
vidH = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('video.avi', fourcc, fps, (vidW, vidH))

# loop runs if capturing has been initialized.
while(True):
	ret, frame = cap.read()
	out.write(frame)

	cv2.imshow('Original', frame)
	if cv2.waitKey(1) & 0xFF == ord('a'):
		break

cap.release()
out.release()
cv2.destroyAllWindows()
