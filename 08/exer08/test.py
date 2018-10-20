import cv2
import numpy as np

scale_filename = "./scales/colorscale_rainbow.jpg"
scale= cv2.imread(scale_filename)

lower_blue = np.array([110,50,50])			# borrowed from https://docs.opencv.org/3.4.2/df/d9d/tutorial_py_colorspaces.html
upper_blue = np.array([130,255,255])

minratio = 0.2
maxratio = 1.0

img_dir = "./Satellite Images/"
img_files = ["albert.jpg", "bret.jpg", "floyd.jpg"]

img_list = [cv2.imread(img_dir + img_name) for img_name in img_files]
hsv_list = [cv2.cvtColor(img, cv2.COLOR_BGR2HSV) for img in img_list]
thr_list = [cv2.inRange(hsv_img, lower_blue, upper_blue) for hsv_img in hsv_list]
res_list = [cv2.bitwise_and(img_list[hsv_list.index(hsv_img)],hsv_img, mask = thr_list[hsv_list.index(hsv_img)]) for hsv_img in hsv_list]
gry_list = [cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) for img in res_list]
out_list = [img.copy() for img in img_list]

for i in range(len(img_files)):
	rows, cols, channels = img_list[i].shape

	for x in range(rows):
		for y in range(cols):
			pixel = gry_list[i][x,y]
			intensity_ratio = pixel/255.0

			if intensity_ratio > minratio:
				map_position = ((intensity_ratio - minratio) / (maxratio - minratio))
				map_position = int(255 * map_position)
				for z in range(channels):
					out_list[i][x,y,z] = scale[0, map_position, z]

for i in range(len(img_files)):
	cv2.imwrite("out_"+img_files[i], out_list[i])
	cv2.imwrite("iso_"+img_files[i], res_list[i])

print("Done!")
# cv2.waitKey(0)
# cv2.destroyAllWindows() 