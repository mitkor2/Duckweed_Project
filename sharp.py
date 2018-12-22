import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())

# load the image
img = cv2.imread(args["image"])
rows,cols,ch = img.shape

pts1 = np.float32([[570,168],[730,168],[100,1600],[1450,1600]])
pts2 = np.float32([[0,0],[200,0],[0,300],[200,300]])

M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(200,300))

plt.subplot(121),plt.imshow(img),plt.title('input')
plt.subplot(122),plt.imshow(dst),plt.title('output')
plt.show()