'''
RUZ, Julianne Marie					2014-04280
GUTIERREZ, Reigner D. 				2014-06096
CMSC 165 U-2L
Exer 04: locate plate numbers in the given three images.
'''

import cv2
import math
import numpy as np

#def 

img = cv2.imread("p1.jpg", 0)
ret, thresh = cv2.threshold(img, 127, 255, 0)
contours = cv2.findContours(thresh, 1, 2)
hierarchy = cv2.findContours(thresh, 1, 2)


cnt = contours[0]
M = cv2.moments(cnt)

cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

area = cv2.contourArea(cnt)
# perimeter = cv2.
print(area)

'''

ERROR LIST:

	Line 26: cv2.error: OpenCV(3.4.2) /io/opencv/modules/imgproc/src/shapedescr.cpp:272: error: (-215:Assertion failed) npoints >= 0 && (depth == 5 || depth == 4) in function 'contourArea'

'''