import qrcode as qrcode
from PIL import Image
# Data to be encoded
data = 'Thanos Alevizos'

# Encoding data using make() function
img = qrcode.make(data)

# Saving as an image file
img.save('TA.png')