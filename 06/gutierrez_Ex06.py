import cv2
import numpy as np 

# for writing text on image
font = cv2.FONT_HERSHEY_SIMPLEX

grayscale = cv2.imread("coins.jpg", 0)
colored = cv2.imread("coins.jpg", 1)

# copy colored image to sizes and result for later use
sizes = colored.copy()
result = colored.copy()

# get the dimensions of the image
height, width = colored.shape[:2]

# process the image
blur = cv2.GaussianBlur(grayscale, (5, 5), 0)
ret, th = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(th, 8)

# total value of coins
val = 0

for i in range(ret):
	# basic
	leftmost_x = stats[i][0]
	topmost_y = stats[i][1]
	width = stats[i][2]
	height = stats[i][3]
	area = stats[i][4]

	#derived
	right_x = leftmost_x + width - 1
	bottom_y = topmost_y + height - 1

	center_x = int(leftmost_x + (width/2))
	center_y = int(topmost_y + (height/2))

	if (92 <= int(width) <= 93):													# 5 cents
		color = [255,0,0]
		val += 0.05
	elif (101 <= int(width) <= 102):												# 10 cents
		color = [0,255,0]
		val += 0.10
	elif (118 <= int(width) <= 121):												# 25 cents
		color = [0,0,255]
		val += 0.25
	elif (141 <= int(width) <= 143):												# P 1
		color = [255,255,0]
		val += 1
	elif (158 <= int(width) <= 159):												# P 5
		color = [255,0,255]
		val += 5
	else:
		continue
		# skip other unwanted components

	# draw bounding boxes to sizes	
	sizes[topmost_y:bottom_y, leftmost_x] = color 									# left 
	sizes[topmost_y, leftmost_x:right_x] = color 									# top
	sizes[topmost_y:bottom_y, right_x] = color 										# right
	sizes[bottom_y, leftmost_x:right_x] = color 									# bottom

	cv2.putText(sizes, str(width), (center_x,center_y), font, 1, color, 2)

# to know the unique widths to determine the acceptable ranges of the width of each kind of coin.
# test = list(set([stats[i][2] for i in range(ret)]))
# print(test)

# for testing
# cv2.imwrite("processed.png", sizes)

# prints the total value of coins on terminal and on the result image
print(val)
cv2.putText(result, str(val), (1157,25), font, 1, [0,0,0], 2)

# result
cv2.imshow("Result", result)
cv2.imwrite("result.png", result)

cv2.waitKey(0)
cv2.destroyAllWindows()