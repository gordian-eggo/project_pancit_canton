'''
RUZ, Julianne Marie					2014-04280
GUTIERREZ, Reigner D. 				2014-06096
CMSC 165 U-2L
Exer 04: locate plate numbers in the given three images.
'''

import cv2
import math
import numpy as np

bw_img = cv2.imread("p3.png", 0)				# read the input image as black and white
out = cv2.imread("p3.png")

ret, thresh = cv2.threshold(bw_img, 127, 255, 0)				# add threshold for binarizing the image
image, contours, hierarchy = cv2.findContours(thresh, 1, 2)		# find contours. Di ko sure kung allowed 'tong function pero wala namang sinabi sa readme na bawal

cnt = contours[1]						# save the desired contour. be warned tho di ko pa makita epekto nito sa output. baka kailangan na RGB yung magiging output

area = cv2.contourArea(cnt)								# get contour area of the desired contour
perimeter = cv2.arcLength(cnt, True)					# get the length of the contour
epsilon = 0.1 * cv2.arcLength(cnt, True)				# epsilon is the accuracy parameter para gumanda yung output
approx = cv2.approxPolyDP(cnt, epsilon, True)			# approximates the contour para pretty siya

print(area)							# print statements, pwedeng tanggalin later
print(perimeter)
print(approx)

bw_img = cv2.drawContours(bw_img, contours, -1, (0, 255, 0), 3)		# draw the contours in green 

cv2.imshow("Original", bw_img)				# show, wait, exit
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("out.jpg", bw_img)

'''

ERROR LIST:

	Line 26: cv2.error: OpenCV(3.4.2) /io/opencv/modules/imgproc/src/shapedescr.cpp:272: error: (-215:Assertion failed) npoints >= 0 && (depth == 5 || depth == 4) in function 'contourArea'
		> fixed 1710H, 9-13-18. Reference: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contours_begin/py_contours_begin.html#contours-getting-started
	
	Error as of 2204H:
		Traceback (most recent call last):
  		File "ruz_gutierrez_Ex04.py", line 23, in <module>
    		cx = int(M['m10']/M['m00'])
		ZeroDivisionError: float division by zero

		Notes: naggaganito lang siya pag yung p3.png yung ipapasa na image. 

NEEDS:

	> isolate the contour for the license plates
	> colorize the photo
	> check if contour really is green
	> gawing function na yung process

LINKS FOR REFERENCE:

	https://docs.opencv.org/3.1.0/dd/d49/tutorial_py_contour_features.html		-		for the functions defined in the readme

'''