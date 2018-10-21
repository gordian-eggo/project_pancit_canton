import cv2
import numpy as np

scale_filename = "./scales/colorscale_rainbow.jpg"
scale= cv2.imread(scale_filename)

# borrowed from https://docs.opencv.org/3.4.2/df/d9d/tutorial_py_colorspaces.html
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

img_dir = "./Satellite Images/"
img_files = ["albert.jpg", "bret.jpg", "floyd.jpg"]

img_list = [cv2.imread(img_dir + img_name) for img_name in img_files]																		# reads the image files from a specified dir
hsv_list = [cv2.cvtColor(img, cv2.COLOR_BGR2HSV) for img in img_list]																		# converts the images to HSV
thr_list = [cv2.inRange(hsv_img, lower_blue, upper_blue) for hsv_img in hsv_list]															# extracts the pixels that qualifies as 'blue' from the images

# for i in range(len(img_files)):
# 	cv2.imwrite(img_files[i], thr_list[i])

# print("Done!")

res_list = [cv2.bitwise_and(img_list[hsv_list.index(hsv_img)],hsv_img, mask = thr_list[hsv_list.index(hsv_img)]) for hsv_img in hsv_list]	# get the extracted pixels from their respective images
res_list = [cv2.cvtColor(img, cv2.COLOR_HSV2BGR) for img in res_list]																		# HSV -> GRAY, since the function only works on grayscale
res_list = [cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) for img in res_list]
res_list = [cv2.applyColorMap(img, cv2.COLORMAP_RAINBOW) for img in res_list]

for i in range(len(img_files)):
	cv2.imwrite(img_files[i], res_list[i])

print("Done!")

out_list = [img.copy() for img in img_list]																									# copies the images for output		