# image processor

import numpy as np
from PIL import Image, ImageDraw
def square_thumb(thum_img,width,height):
    if height == width:
        return thum_img
    elif height > width:
        square_img = Image.new(thum_img.mode, (height, height))
        square_img.paste(thum_img, ((height - width) // 2,0))
        return square_img
    else:
        square_img = Image.new(thum_img.mode, (width, width))
        square_img.paste(thum_img, (0, (width - height) // 2))
        return square_img 

def processor(image,fe):
    img=Image.open(image)
    w,h = img.size
    img = square_thumb(img, w,h)
    npImage=np.array(img)
    h,w=img.size
    alpha = Image.new('L', img.size,0)
    draw = ImageDraw.Draw(alpha)
    draw.pieslice([0,0,h,w],0,360,fill=255)
    npAlpha=np.array(alpha)
    npImage=np.dstack((npImage,npAlpha))
    Image.fromarray(npImage).resize((119,119)).save(fe+'.png')

##for i in range(1,21):
##    f = str(i)+".png"
##    processor(f,str(i+22))
    
def proc2(image):
    Image.open(image).resize((139,136)).save(image)
    
for i in range(1,7):
    f = "sp"+str(i)+".png"
    proc2(f)
