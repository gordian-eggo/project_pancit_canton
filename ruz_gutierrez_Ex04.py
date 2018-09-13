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
# contours = cv2.findContours(thresh, 1, 2)
image, contours, hierarchy = cv2.findContours(thresh, 1, 2)


cnt = contours[0]
M = cv2.moments(cnt)

cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

area = cv2.contourArea(cnt)
perimeter = cv2.arcLength(cnt, True)
epsilon = 0.1 * cv2.arcLength(cnt, True)
approx = cv2.approxPolyDP(cnt, epsilon, True)

print(cx, cy)
print(area)
print(perimeter)
print(approx)

img = cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

cv2.imshow("Original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''

ERROR LIST:

	Line 26: cv2.error: OpenCV(3.4.2) /io/opencv/modules/imgproc/src/shapedescr.cpp:272: error: (-215:Assertion failed) npoints >= 0 && (depth == 5 || depth == 4) in function 'contourArea'
		> fixed 1710H, 9-13-18. Reference: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contours_begin/py_contours_begin.html#contours-getting-started

'''