from os import listdir
from PIL import Image
from numpy import asarray
from matplotlib import pyplot
from mtcnn.mtcnn import MTCNN
import cv2

folder = 'faceGenerator/'
i=1
#requiredSize=(160,160)
for filename in listdir(folder):
	path = folder + filename

	#get face
	image = Image.open(path)
	pixels = asarray(image)
	detector = MTCNN()
	results = detector.detect_faces(pixels)
	print(len(results))

	for j in range(len(results)):
		# print(i)
		x1,y1,width,height = results[j]['box']
		print(x1,y1,width,height)
		x1, y1 = abs(x1), abs(y1)

		x2,y2 = x1+width, y1+height

		face = pixels[y1:y2, x1:x2]
		
		# print(i, face.shape)
		image = Image.fromarray(face)
		#image = image.resize(requiredSize)
		face_array = asarray(image)

		#pyplot.subplot(2,7,i)
		#pyplot.axis('off')
		#pyplot.imshow(face)
		i += 1

		cv2.imwrite('face/'+str(i)+'_'+str(x1)+'_'+str(y1)+'_'+str(x2)+'_'+str(y2)+'_'+'_faces.jpg',face)

	j=0	
#pyplot.show()	