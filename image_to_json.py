import json
import os
import base64

data = open('wharf-rotated-small.png', "rb").read()  
encoded = base64.encodebytes(data).decode()
input_data = json.dumps({'data': str(encoded)})