import cv2
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
from pyimagesearch import four_point_transform
from picamera import PiCamera
from time import sleep
# load the image and grab the source coordinates (i.e. the list of
# of (x, y) points)
# NOTE: using the 'eval' function is bad form, but for this example
# let's just roll with it -- in future posts 
# automatically determine the coordinates without pre-supplying them
pts1 = np.array(eval('[(141, 68), (186, 71), (276, 473), (33, 478)]'), dtype = "float32")
pts2 = np.array(eval('[(294, 272), (399, 270), (306, 334), (339, 329)]'), dtype = "float32")
pts3 = np.array(eval('[(680, 74), (730, 90), (793, 467), (610, 462)]'), dtype = "float32")
def camera():
	camera = PiCamera()
	camera.capture('threepots.png')
def warpedfoo(image, pts):
	# apply the four point tranform to obtain a "birds eye view" of
	# the image
	warped = four_point_transform(image, pts)
	return warped
def changecolorandframe(img1):
	BLUE = [255,0,0]
	constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)
	hsv = cv2.cvtColor(constant,cv2.COLOR_BGR2RGB)
	#plt.imshow(constant,'gray'),plt.title('CONSTANT')#1
	#plt.show()
	return hsv
def colordetection(color_changed,boundaries):
	# define the list of boundaries #boundaries = [([0, 0, 240], [10, 10, 255]),([100, 80, 60], [145, 135, 130])]
	# loop over the boundaries
	for (lower, upper) in boundaries:
		# create NumPy arrays from the boundaries
		lower = np.array(lower, dtype = "uint8")
		upper = np.array(upper, dtype = "uint8")
		# find the colors within the specified boundaries and apply
		# the mask
		mask = cv2.inRange(color_changed, lower, upper)
		colordet_img = cv2.bitwise_and(color_changed, color_changed, mask = mask)
		# show the images
		#cv2.imshow("images", np.hstack([color_changed, colordet_img]))
		#cv2.waitKey(0)
	return colordet_img
def determprocentege(path):
	im = Image.open(path)
	black = 0
	other_color = 0

	for pixel in im.getdata():
		if pixel == (0, 0, 0): # if your image is RGB (if RGBA, (0, 0, 0, 255) or so
			black += 1
		else:
			other_color += 1
	#print('black=' + str(black)+', red='+str(other_color))
	covered_proc = 100*(float(other_color)/float((other_color+black)))
	return covered_proc
camera()
image = cv2.imread('threepots.png') 
img1 = warpedfoo(image, pts1)
img2 = warpedfoo(image, pts2)
img3 = warpedfoo(image, pts3)
color_changed1 = changecolorandframe(img1)
color_changed2 = changecolorandframe(img2)
color_changed3 = changecolorandframe(img3)
colordet_red1 = colordetection(color_changed1,[([0, 0, 240], [10, 10, 255])])
colordet_red2 = colordetection(color_changed2,[([0, 0, 240], [10, 10, 255])])
colordet_red3 = colordetection(color_changed3,[([0, 0, 240], [10, 10, 255])])
colordet_flower1 = colordetection(color_changed1,[([100, 80, 60], [145, 135, 130])])
colordet_flower2 = colordetection(color_changed2,[([100, 80, 60], [145, 135, 130])])
colordet_flower3 = colordetection(color_changed3,[([100, 80, 60], [145, 135, 130])])
cv2.imwrite('img1.jpg',colordet_flower1)
cv2.imwrite('img2.jpg',colordet_flower2)
cv2.imwrite('img3.jpg',colordet_flower3)
path1 = 'img1.jpg'
path2 = 'img2.jpg'
path3 = 'img3.jpg'
precentage1 = determprocentege(path1)
precentage2 = determprocentege(path2)
precentage3 = determprocentege(path3)
#print(precentage1,precentage2,precentage3)
print precentage1,",",precentage2,",",precentage3
#cv2.imshow("Flower", colordet_flower)
#cv2.waitKey(0)
