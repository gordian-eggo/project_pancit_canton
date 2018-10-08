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
cropped3 = cropped3[245:315, 340:490]
cropped.append(cropped3)

# loop through the images to process them
for i in range(0,3):
	# cv2.imshow("p"+str(i), cropped[i])
	# clean
	cropped[i] = cv2.blur(cropped[i],(5,5))
	# get connected components
	ret, labels, stats, centroids = cv2.connectedComponentsWithStats(cropped[i], 8)
	# loop through each component to determine character
	for i in range(1, ret):
		# get component stats
		t = stats[i, cv2.CC_STAT_TOP];
		b = t + stats[i, cv2.CC_STAT_HEIGHT] -1;
		l = stats[i, cv2.CC_STAT_LEFT];
		r = l + stats[i, cv2.CC_STAT_WIDTH] -1;
		
		# crop components
		well = cropped[i][t-5:b+5, l-5:r+5]
		cv2.imshow("he{}".format(i), well)
		# prints character detected
		print(pytesseract.image_to_string(well, config="--psm 7"))

cv2.waitKey(0)
cv2.destroyAllWindows()