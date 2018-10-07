'''
RUZ, Julianne Marie					2014-04280
GUTIERREZ, Reigner D. 				2014-06096
CMSC 165 U-2L
Exer 04: locate plate numbers in the given three images.
'''

import cv2
import math
import numpy as np

images = ["p1.jpg", "p2.jpg", "p3.png"]

def findRectangularContours(cnt):
	area = cv2.contourArea(cnt)																			# get contour area of the desired contour
	perimeter = cv2.arcLength(cnt, True)																# get the length of the contour
	epsilon = 0.02 * perimeter 																			# epsilon is the accuracy parameter para gumanda yung output
	approx = cv2.approxPolyDP(cnt, epsilon, True)														# approximates the contour para pretty siya

	# insert if-statement here with sufficient criteria to filter out most contours
	return cnt

def findPlate(img):
	bw_img = cv2.imread(img, 0)																			# read the input image as black and white
	out = cv2.imread(img)
	ret, thresh = cv2.threshold(bw_img, 127, 255, 0)													# add threshold for binarizing the image
	image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)		# find contours

	for cnt in contours:
		if findRectangularContours(cnt).all():
			bw_img = cv2.drawContours(out, [cnt], -1, (0,255,0), 3)										# draw the contours in green 


	return out

for image in images:
	output_img = findPlate(image)
	cv2.imshow("Result output of " + image, output_img)
	cv2.imwrite("out_" + image, output_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

'''
LINKS FOR REFERENCE:

	https://docs.opencv.org/3.1.0/dd/d49/tutorial_py_contour_features.html						-		for the functions defined in the readme
	https://learndeltax.blogspot.com/2016/02/number-plate-detection-in-opencv-python.html		-		for the criteria for the filter

'''