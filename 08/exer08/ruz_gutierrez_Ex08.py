import cv2
import numpy as np

sat_imgs = [] 
hsv_satellite = []
lower_blue = np.array([110,50,50])			# borrowed from https://docs.opencv.org/3.4.2/df/d9d/tutorial_py_colorspaces.html
upper_blue = np.array([130,255,255])

albert = cv2.imread("albert.jpg")			# nilabas ko siya sa Satellite images folder kasi nagkakaloko sa pagkuha 
sat_imgs.append(albert)

bret = cv2.imread("bret.jpg")
sat_imgs.append(bret)

floyd = cv2.imread("floyd.jpg")
sat_imgs.append(floyd)

# followed steps here:
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html
for img in sat_imgs:					
	hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	threshold = cv2.inRange(hsv_img, lower_blue, upper_blue)
	res = cv2.bitwise_and(img, hsv_img, mask = threshold)
	cv2.imshow("img", img)
	cv2.imshow("threshold", threshold)
	cv2.imshow("res", res)
	# output at this point is pretty good, very close to what we're looking for

# yung pseudocoloring sundan mo na lang sa pseudocoloring-manual.py

cv2.waitKey(0)
cv2.destroyAllWindows()