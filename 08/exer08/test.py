import cv2
import numpy as np

scale_filename = "./scales/colorscale_rainbow.jpg"
scale= cv2.imread(scale_filename)

lower_blue = np.array([110,50,50])			# borrowed from https://docs.opencv.org/3.4.2/df/d9d/tutorial_py_colorspaces.html
upper_blue = np.array([130,255,255])

minsat = lower_blue[1]						# minimum saturation of lower_blue
maxsat = upper_blue[1]						# maximum saturation of upper_blue

img_dir = "./Satellite Images/"
img_files = ["albert.jpg", "bret.jpg", "floyd.jpg"]

print("Fixing file lists...")
img_list = [cv2.imread(img_dir + img_name) for img_name in img_files]																		# reads the image files from a specified dir
hsv_list = [cv2.cvtColor(img, cv2.COLOR_BGR2HSV) for img in img_list]																		# converts the images to HSV
thr_list = [cv2.inRange(hsv_img, lower_blue, upper_blue) for hsv_img in hsv_list] 															# extracts the pixels that qualifies as 'blue' from the images
res_list = [cv2.bitwise_and(img_list[hsv_list.index(hsv_img)],hsv_img, mask = thr_list[hsv_list.index(hsv_img)]) for hsv_img in hsv_list]	# get the extracted pixels from their respective images
res_list = [cv2.cvtColor(img, cv2.COLOR_BGR2HSV) for img in res_list]
out_list = [img.copy() for img in img_list]																									

print("Adjusting value...")
# this is naturally slow
for i in range(len(img_files)):
	rows, cols, channels = img_list[i].shape

	for x in range(rows):
		for y in range(cols):
			# this changes the criteria to value instead of intensity
			pixel = res_list[i][x,y]
			
			value = pixel[2]

			if value > minsat:
				map_position = ((value - minsat) / (maxsat - minsat))
				map_position = int(255 * map_position)
				for z in range(channels):
					if (map_position <= 255 and map_position > 253):				# reds
						out_list[i][x,y,z] = scale[0, 0, z]
					elif (map_position <= 60 and map_position >= 40):			# oranges
						out_list[i][x,y,z] = scale[0, 0, z]
					elif (map_position > 60 and map_position <= 120):			# yellows
						out_list[i][x,y,z] = scale[0, 36, z]
					elif (map_position > 120 and map_position <= 180):			# greens
						out_list[i][x,y,z] = scale[0, 219, z]
					elif (map_position > 180 and map_position <= 200):			# blues
						out_list[i][x,y,z] = scale[0, 255, z]
					elif (map_position > 200 and map_position <= 255):			# purples
						out_list[i][x,y,z] = scale[0, 255, z]
					# orange, yellow, green, and blue values were adjusted to try to get a result closer 
					# to what the exercise specfications state


print("Writing to file...")
for i in range(len(img_files)):
	cv2.imwrite("out_"+img_files[i], out_list[i])
	cv2.imwrite("iso_"+img_files[i], res_list[i])

print("Done!")