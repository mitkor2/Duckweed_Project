# import the necessary packages
from pyimagesearch import four_point_transform
import numpy as np
import argparse
import cv2

# load the image and grab the source coordinates (i.e. the list of
# of (x, y) points)
# NOTE: using the 'eval' function is bad form, but for this example
# let's just roll with it -- in future posts I'll show you how to
# automatically determine the coordinates without pre-supplying them
image = cv2.imread('pic2.jpg') 
pts = np.array(eval('[(67, 685), (597, 661), (378, 87), (281, 91)]'), dtype = "float32")
def warpedfoo(image, pts):
	# apply the four point tranform to obtain a "birds eye view" of
	# the image
	warped = four_point_transform(image, pts)
	 
	# show the original and warped images
	#cv2.imshow("Original", image)
	#cv2.imshow("Warped", warped)
	cv2.waitKey(0)
	return warped
warped = warpedfoo(image, pts)
cv2.imshow("Warped", warped)
cv2.waitKey(0)


