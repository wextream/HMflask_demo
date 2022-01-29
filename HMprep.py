import numpy as np
from PIL import  Image
import scipy.ndimage as ndimage
import random

def HM_matrix(image,gaussian_std=10):

    image = Image.open(image)
    width, height = image.size

    heat_map = np.random.uniform(low=0,high=50,size=(105,92))
    ke1 = np.array([[random.randint(40,65),random.randint(50,80)]])
    for k in range (0,92):
        for h in range (0,105):
            cor = np.array([[h,k]])
            rad1 = np.linalg.norm(ke1-cor)
            if rad1 < 10:
                pm_val1 = ((10-rad1)/10)*255
                heat_map[h,k] += pm_val1
    heatmap_image = Image.fromarray(heat_map)
    heatmap_image_resized = heatmap_image.resize((width,height))
    heatmap_image_resized = ndimage.gaussian_filter(heatmap_image_resized, 
                                                        sigma=(gaussian_std, gaussian_std), 
                                                        order=0)
    heatmap_image_resized = np.asarray(heatmap_image_resized)

    return image , heatmap_image_resized


