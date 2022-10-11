

# import base64
# with open("2.jpg", "rb") as img_file:
#     my_string = base64.b64encode(img_file.read())
# print(my_string)


from PIL import Image
from io import BytesIO
import base64

crop_file = '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'

base64_img_bytes = crop_file.encode('utf-8')
with open('decoded_image.png', 'wb') as file_to_save:
    decoded_image_data = base64.decodebytes(base64_img_bytes)
    file_to_save.write(decoded_image_data)