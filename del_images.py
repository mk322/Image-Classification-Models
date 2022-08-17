import os
import numpy as np
from PIL import Image

img_size = 224
labels = []
#images = np.empty([0, img_size*img_size*3])
count = 0
for lab in [0,1,2,3,4]:
    path = f"Images/{lab+1}"
    for i in range(len(os.listdir(path))):
        #if i == 27:
        img = np.array(Image.open(f"Images/{lab+1}/class{lab+1}_{i}.jpeg").resize(size=(img_size, img_size)))
        if (img.shape[0] != img_size) or (img.shape[1] != img_size) or (len(img.shape) != 3):
            os.remove(f"Images/{lab+1}/class{lab+1}_{i}.jpeg")
            print('delete')
        #img = img.reshape((1, img_size*img_size*3))
        #labels.append(lab)
        #images = np.append(images, img, axis=0)
    #print(images.shape)
    count += len(os.listdir(path))

print(count)