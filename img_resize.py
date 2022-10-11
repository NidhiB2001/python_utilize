import cv2


img_name = '10-09-2022_18:19:14_jRM.png'
 
img = cv2.imread(img_name)

# Get original height and width
print(f"Original Dimensions : {img.shape}")

# resize image by specifying custom width and height
resized = cv2.resize(img, (146,36))

print(f"Resized Dimensions : {resized.shape}")
# cv2.imwrite('resized_imaged.jpg', resized)

cv2.imwrite('resized_'+img_name, resized)