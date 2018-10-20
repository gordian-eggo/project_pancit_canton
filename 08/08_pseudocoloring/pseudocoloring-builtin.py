'''
	author: ceposerio@up.edu.ph
	description: a demo for using the built-in function for pseudocoloring
	References: Color map types: https://docs.opencv.org/3.4/d3/d50/group__imgproc__colormap.html#ga9a805d8262bcbe273f16be9ea2055a65
'''

import numpy as np 
import cv2

colormap_names = {cv2.COLORMAP_AUTUMN: "COLORMAP_AUTUMN",
cv2.COLORMAP_BONE: "COLORMAP_BONE",
cv2.COLORMAP_JET: "COLORMAP_JET",
cv2.COLORMAP_WINTER: "COLORMAP_WINTER",
cv2.COLORMAP_RAINBOW: "COLORMAP_RAINBOW",
cv2.COLORMAP_OCEAN: "COLORMAP_OCEAN",
cv2.COLORMAP_SUMMER: "COLORMAP_SUMMER",
cv2.COLORMAP_SPRING: "COLORMAP_SPRING",
cv2.COLORMAP_COOL: "COLORMAP_COOL",
cv2.COLORMAP_HSV: "COLORMAP_HSV",
cv2.COLORMAP_PINK: "COLORMAP_PINK",
cv2.COLORMAP_HOT: "COLORMAP_HOT",
cv2.COLORMAP_PARULA: "COLORMAP_PARULA"}


INPUT_FILENAME = "lily.jpg"
src = cv2.imread(INPUT_FILENAME,0)
out = np.zeros_like(src)


for i in range(12):
	result = cv2.applyColorMap(src, i)
	cv2.imshow(colormap_names[i], result)

cv2.imshow("Original", src)
cv2.waitKey(0)
cv2.destroyAllWindows()