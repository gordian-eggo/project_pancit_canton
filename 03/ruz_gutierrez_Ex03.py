'''
RUZ, Julianne Marie						2014-04280
GUTIERREZ, Reigner D. 					2014-06096
CMSC 165 U-2L
Exer 03: Implement the mean, median, and Gaussian filters.
'''
import cv2
import math
import numpy as np 

img = cv2.imread("saltAndPepper.jpg", 0)

def meanfilter(img, kernelSize):
	x = int(kernelSize/2)
	# pads the image to avoid NaN values
	padded_img = cv2.copyMakeBorder(img, x, x, x, x, cv2.BORDER_CONSTANT, value=(0.0,0.0,0.0))

	out = img.copy()

	# get the mean for every pixel
	for i in range(0, out.shape[0]-x):
		for j in range(1, out.shape[1]-x):
			img_slice = padded_img[i-x:i+x, j-x:j+x].copy().flatten()
			out[i,j] = np.nanmean(img_slice, dtype="int")

	return out

def medianfilter(img, kernelSize):
	x = int(kernelSize/2)

	padded_img = cv2.copyMakeBorder(img, x, x, x, x, cv2.BORDER_CONSTANT, value=(0.0,0.0,0.0))

	out = img.copy()

	for i in range(0, out.shape[1]-x):
		for j in range(1, out.shape[1]-x):
			img_slice = padded_img[i-x:i+x, j-x:j+x].copy().flatten()
			# print(i,j)
			# print(img_slice)
			img_slice[np.isnan(img_slice)] = 0
			# this is supposed to typecast the float as an integer
			# out[i,j] = math.trunc(np.nanmedian(img_slice, axis=None, out=None, overwrite_input=False, keepdims=False))

	return out

def weightedmeanfilter(img, kernelSize):
	x = int(kernelSize/2)

	# copied from mean filter
	padded_img = cv2.copyMakeBorder(img, x, x, x, x, cv2.BORDER_CONSTANT, value=(0.0,0.0,0.0))

	out = img.copy()

	for i in range(0, out.shape[0]-x):
		for j in range(1, out.shape[1]-x):
			img_slice = padded_img[i-x:i+x, j-x:j+x].copy().flatten()
			#out[i,j] = np.nanweightedmean(img_slice, dtype="int")

	return out

#cv2.imshow("Median Filter", medianfilter(img, 3))
cv2.imshow("Mean Filter", meanfilter(img, 3))
cv2.imshow("Weighted Mean Filter", weightedmeanfilter(img, 3))

cv2.waitKey(0)
cv2.destroyAllWindows()

