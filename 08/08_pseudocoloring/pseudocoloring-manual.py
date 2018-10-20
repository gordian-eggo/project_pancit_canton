'''
	author: ceposerio@up.edu.ph
	description: an implementation of pseudocoloring with intensity slicing
	References: Color map types: https://docs.opencv.org/3.4/d3/d50/group__imgproc__colormap.html#ga9a805d8262bcbe273f16be9ea2055a65
'''
import cv2
import numpy as np 


INPUT_FILENAME = 'lily.jpg'
SCALE_FILENAME = "./scales/colorscale_ocean.jpg"
src = cv2.imread(INPUT_FILENAME) # colored
scale = cv2.imread(SCALE_FILENAME) # colored

out = src.copy()
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY) # convert input to gray scale


minratio = 0.6
maxratio = 1.0

rows,cols,channels = src.shape

print(scale.shape)
print(scale[0,0])
print(scale[0,255])

for i in range(rows):
	for j in range(cols):
		
		# gray value at pixel i,j
		pixel = gray[i,j]
		intensity_ratio = pixel/255.0 # possible value of intensity_ratio will be [0,1]

		# perform intensity slicing -- if within min and max, assign a pseudo color
		if intensity_ratio > minratio: 
			map_position = ((intensity_ratio-minratio)/(maxratio-minratio))	# normalize value to be within the range [0,1]	
			map_position = int(255 * map_position) # scale value to be [0,255]
			for c in range(channels):
				# assign corresponding value in the colorscale
				out[i,j,c] = scale[0,map_position,c]


cv2.imshow("Original", src)
cv2.imshow("Scale", scale)
cv2.imshow("Transformed", out)

cv2.waitKey(0)
cv2.destroyAllWindows()