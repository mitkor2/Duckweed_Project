from picamera import PiCamera #importing functions from libraries
from time import sleep
import numpy as np
import argparse
import cv2
import os
import shutil
import stat

folder_pic = '/home/pi/Duckweed'
input_path = '/home/pi/Duckweed/Pic'
os.mkdir(folder_pic)
os.mkdir(input_path)
os.chmod(folder_pic, stat.S_IXOTH | stat.S_IWOTH | stat.S_IROTH  | stat.S_IREAD | stat.S_IWRITE | stat.S_IEXEC | stat.S_IRWXO)
os.chmod(input_path, stat.S_IXOTH | stat.S_IWOTH | stat.S_IROTH  | stat.S_IREAD | stat.S_IWRITE | stat.S_IEXEC | stat.S_IRWXO)
from os.path import join

camera = PiCamera()

camera.start_preview()
sleep(5)
camera.capture('/home/pi/Duckweed/Pic/image.jpg')
camera.stop_preview()
