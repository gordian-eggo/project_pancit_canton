import numpy as np 
import math
import cv2

images = ["p1.jpg", "p2.jpg", "p3.png"]
bin_images = []
cropped = []

def binarize(img):
	img = cv2.imread(img, 0)
	ret, binarized = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
	bin_images.append(binarized)

for image in images:
	binarize(image)

# crop out the license plate for p1.jpg
cropped1 = bin_images[0]
cropped1 = cropped1[134:179, 105:325]
cropped.append(cropped1)

# crop out the license plate for p2.jpg
cropped2 = bin_images[1]
cropped2 = cropped2[165:205, 341:456]
cropped.append(cropped2)

# crop out the license plate for p3.png
cropped3 = bin_images[2]
cropped3 = cropped3[340:490, 245:315]
cropped.append(cropped3)
# pa-edit na lang huhu it's far from accurate

# see .cpp file for nexgt steps


cv2.imshow("p1", cropped[0])
cv2.imshow("p2", cropped[1])
cv2.imshow("p3", cropped[2])

cv2.waitKey(0)
cv2.destroyAllWindows()