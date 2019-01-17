import cv2
import numpy as np
from matplotlib import pyplot as plt
from pyimagesearch import four_point_transform
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
	return warped
def changecolorandframe(img1):
	BLUE = [255,0,0]
	
	constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)

	hsv = cv2.cvtColor(constant,cv2.COLOR_BGR2RGB)
	plt.imshow(constant,'gray'),plt.title('CONSTANT')
	plt.show()
	return hsv
def colordetection(color_changed):
	# define the list of boundaries
	boundaries = [
		([34, 55, 100], [127, 151, 175]),
		([27, 27, 27], [190, 181, 177]),
		([103, 86, 65], [145, 133, 128]),
		([160,20,70], [190,255,255])

	]

	# loop over the boundaries
	for (lower, upper) in boundaries:
		# create NumPy arrays from the boundaries
		lower = np.array(lower, dtype = "uint8")
		upper = np.array(upper, dtype = "uint8")
		
		# find the colors within the specified boundaries and apply
		# the mask
		mask = cv2.inRange(color_changed, lower, upper)
		colordet_img = cv2.bitwise_and(color_changed, color_changed, mask = mask)
		_, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
		
		# show the images
		cv2.imshow("mask", mask)
		cv2.imshow("images", np.hstack([color_changed, colordet_img]))
		cv2.waitKey(0)
	return colordet_img
img1 = warpedfoo(image, pts)
color_changed = changecolorandframe(img1)
colordet_img = colordetection(color_changed)
cv2.imshow("Warped", color_changed)
cv2.waitKey(0)