#pip install rembg 
#pip install PIL

from rembg import remove
from PIL import Image

input = 'file.jpg'
output= 'file.png'

inp = Image.open(input)
out=remove(inp)
out.save(output)