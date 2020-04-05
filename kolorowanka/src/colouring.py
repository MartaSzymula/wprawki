from skimage import io
from PIL import Image
from skimage.color import rgb2gray
from skimage.morphology import thin
from skimage.filters import threshold_local, threshold_otsu
import numpy as np
from matplotlib import pyplot as plt

my_im = io.imread("../images/img3.jpg")

grey = rgb2gray(my_im)

io.imshow(grey)
plt.show()

thresh = threshold_otsu(grey)
binary = grey > thresh

io.imshow(binary)
plt.show()

drawing = thin(binary)

io.imshow(drawing)
plt.show()


# drawing.save("../images/drawing.png")
# Image.fromarray(drawing).show()
