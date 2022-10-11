# Write Python code here
# import the necessary packages
import cv2
import argparse

# now let's initialize the list of reference point
ref_point = []
crop = False

def shape_selection(event, x, y, flags, param):
	# grab references to the global variables
	global ref_point, crop

	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping is being performed
	if event == cv2.EVENT_LBUTTONDOWN:
		ref_point = [(x, y)]

	# check to see if the left mouse button was released
	elif event == cv2.EVENT_LBUTTONUP:
		# record the ending (x, y) coordinates and indicate that
		# the cropping operation is finished
		ref_point.append((x, y))

		# draw a rectangle around the region of interest
		cv2.rectangle(image, ref_point[0], ref_point[1], (0, 255, 0), 2)
		cv2.imshow("image", image)


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help ="Path to the image")
args = vars(ap.parse_args())

# load the image, clone it, and setup the mouse callback function
image = cv2.imread(args["image"])
#percent by which the image is resized
scale_percent = 20

#calculate the 50 percent of original dimensions
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)

# dsize
dsize = (width, height)

# resize image
image = cv2.resize(image, dsize)

clone = image.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", shape_selection)


# keep looping until the 'q' key is pressed
while True:
	# display the image and wait for a keypress
	cv2.imshow("image", image)
	key = cv2.waitKey(1) & 0xFF

	# press 'r' to reset the window
	if key == ord("r"):
		image = clone.copy()

	# if the 'c' key is pressed, break from the loop
	elif key == ord("c"):
		break

if len(ref_point) == 2:
    crop_img = clone[ref_point[0][1]:ref_point[1][1], ref_point[0][0]:
														ref_point[1][0]]
    cv2.imshow("crop_img", crop_img)
    cv2.imwrite('crop.jpg', crop_img)
    cv2.waitKey(0)
    
  #  Now after selecting a proper selection like above, just press ‘c’ to extract, as programmed.
  #First select the desired portion from the image. In addition, we can remove bad selection by pressing ‘r’ as programmed for making a new proper selection.

# close all open windows
cv2.destroyAllWindows()
