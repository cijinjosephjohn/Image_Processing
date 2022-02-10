from PIL import Image

img = Image.open('sunflower.jpg')

width, height = img.size
t= height/2
m = 3* height/4
img1 = img.crop((50,t,164,m))

img1.show()