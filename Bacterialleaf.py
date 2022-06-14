from PIL import Image
import numpy as np
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import glob


def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

image_list = []

for filename in glob.glob('/Users/abbas/Downloads/train_images/bacterial_leaf_blight/*.jpg'): #assuming gif
    #im=Image.open(filename)
    img = mpimg.imread(filename)    
    im = rgb2gray(img)    
    #image_sequence = im.getdata()
    image_array = np. array(im)
    image_array=image_array.reshape(307200)
    image_list.append(image_array)
   
arr = np.array(image_list)
df= pd.DataFrame(arr)
