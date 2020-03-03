from PIL import Image
import os

def enemy():
    size = (50,50)
    for i in range(1,6):
        f = 'image/plane/{}.png'.format(str(i))
        im = Image.open(f)
        im.thumbnail(size, Image.ANTIALIAS)
        im.save('image/plane/p{}.png'.format(str(i)))

def hero():
    size = (80,80)
    f = 'image/plane/heroplane1.png'
    im = Image.open(f)
    im.thumbnail(size, Image.ANTIALIAS)
    im.save('image/plane/heroplane.png')

hero()
