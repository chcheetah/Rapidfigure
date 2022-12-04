# image processor

import numpy as np
from PIL import Image, ImageDraw

# function to generate squared image
def square_thumb(thum_img,width,height):
    
    # checking if height and width are
    # are equal then return image as it is
    if height == width:
        return thum_img
  
    # checking if height is greater than width
    elif height > width:
        
        # creating the new mask image of size i,e height of Image
        square_img = Image.new(thum_img.mode, (height, height))
          
        # pasting the original image on mask image
        # using paste() function to make it square
        square_img.paste(thum_img, ((height - width) // 2,0))
          
        # returning the generated square image
        return square_img
  
    # if width is greater than height
    else:
        
        # creating the new mask image of size i,e width of Image
        square_img = Image.new(thum_img.mode, (width, width))
          
        # pasting the original image on mask image using paste()
        # function to make it square
        square_img.paste(thum_img, (0, (width - height) // 2))
          
        # returning the generated square image
        return square_img 
  


# Open the input image as numpy array, convert to RGB
img=Image.open("dog.jpg")
w,h = img.size
img = square_thumb(img, w,h)
npImage=np.array(img)
h,w=img.size

# Create same size alpha layer with circle
alpha = Image.new('L', img.size,0)
draw = ImageDraw.Draw(alpha)
draw.pieslice([0,0,h,w],0,360,fill=255)

# Convert alpha Image to numpy array
npAlpha=np.array(alpha)

# Add alpha layer to RGB
npImage=np.dstack((npImage,npAlpha))

# Save with alpha
Image.fromarray(npImage).resize((119,119)).save('result.png')


