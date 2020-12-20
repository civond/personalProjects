import cv2
from google.colab.patches import cv2_imshow
import numpy as np
from scipy.ndimage import maximum_filter, minimum_filter
from PIL import Image

img = cv2.imread('camasLily.jpg')
blue, green, red = cv2.split(img) #splits img into separate channels
grayscale = cv2.imread('camasLily.jpg', cv2.IMREAD_GRAYSCALE) # Convert image to grayscale

#Image Properties
#print("- Number of Pixels: " + str(img.size))
#print("- Shape/Dimensions: " + str(img.shape))

#cv2_imshow(red) # red channel
#cv2_imshow(blue) # blue channel
#cv2_imshow(green) # green channel
#cv2_imshow(img_gs) # grayscale

#cv2.imwrite('camasRed.jpg',red)
#cv2.imwrite('camasGreen.jpg',green)
#cv2.imwrite('camasBlue.jpg',blue)
cv2.imwrite('camasGrey.jpg',grayscale)

def thresholding():
    gsimg = cv2.imread('camasGrey.jpg', 0)

    # binary thresholding on image with T = 125
    r, threshold = cv2.threshold(gsimg, 125, 255, cv2.THRESH_BINARY)
    cv2_imshow(threshold)
    cv2.imwrite('camasThreshold.jpg',threshold)

def salt_pepper(prob):
      #SP noise ratio
      spr = 0.5
      output = np.copy(grayscale)

      #salt noise on each pixel individually
      num_salt = np.ceil(prob * grayscale.size * spr)
      coords = [np.random.randint(0, i - 1, int(num_salt))
            for i in grayscale.shape]
      output[coords] = 1

      #pepper noise on each pixel individually
      num_pepper = np.ceil(prob * grayscale.size * (1. - spr))
      coords = [np.random.randint(0, i - 1, int(num_pepper))
            for i in grayscale.shape]
      output[coords] = 0
      cv2_imshow(output)
      return output

def kernelSharpening():
    # Create our sharpening kernel, the sum of all values must equal to one for uniformity
    kernel_sharpening = np.array([[-1,-1,-1],
                                  [-1, 9,-1],
                                  [-1,-1,-1]])

    # Applying filter on image with salt & pepper noise
    sharpened_img = cv2.filter2D(spr_05, -1, kernel_sharpening)
    cv2_imshow(sharpened_img)
    cv2.imwrite('kernelSharpened.jpg', sharpened_img)

def midpoint(img):
    maxf = maximum_filter(img, (3, 3))
    minf = minimum_filter(img, (3, 3))
    midpoint = (maxf + minf) / 2
    cv2_imshow(midpoint)
    cv2.imwrite('midpoint.jpg', midpoint)

def contraharmonic_mean(img, size, Q):
    num = np.power(img, Q + 1)
    denom = np.power(img, Q)
    kernel = np.full(size, 1.0)
    result = cv2.filter2D(num, -1, kernel) / cv2.filter2D(denom, -1, kernel)
    return result

thresholding()
spr_05 = salt_pepper(0.5)
cv2.imwrite('sp.jpg', spr_05)

kernelSharpening()
midpoint(spr_05)
contraharmonic_mean(spr_05, (3,3), 0.5)
cv2.imwrite('contraharmonic_mean.jpg', contraharmonic_mean(spr_05, (3,3), 0.5))

