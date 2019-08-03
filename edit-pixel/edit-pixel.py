import glob
from PIL import Image

files = glob.glob('./edit/*')

for i, f in enumerate(files):
    img = Image.open('./edit/pic' + str(i) + '.JPG')
    width,height=1000,666
    img = img.resize((width,height))
    img.save('./fin/pic_resize' + str(i) + '.JPG')
