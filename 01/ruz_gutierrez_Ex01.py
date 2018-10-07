import cv2
import numpy as np
                                                                       
filename = "input_02.jpg"				# read the shuffled photo 

image = cv2.imread(filename)
output_file = cv2.imread(filename)

windowName = "CMSC 165 EXER 01"
cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)

# coordinates for reshuffling
# [0] 0:128		
# [1] 128:256
# [2] 256:384
# [3] 384:512
																		# from 	   -> to
output_file[0:128, 256:384] 	= image[0:128, 0:128].copy()			# 0,0 (1)  -> 0,2 (3)
output_file[384:512, 384:512] 	= image[0:128, 128:256].copy()			# 0,1 (2)  -> 3,3 (16)
output_file[128:256, 128:256] 	= image[0:128, 256:384].copy()			# 0,2 (3)  -> 1,1 (6)
output_file[384:512, 0:128] 	= image[0:128, 384:512].copy()			# 0,3 (4)  -> 3,0 (13)

output_file[256:384, 128:256] 	= image[128:256, 0:128].copy()			# 1,0 (5)  -> 2,1 (10)
output_file[384:512, 256:384] 	= image[128:256, 128:256].copy()		# 1,1 (6)  -> 3,2 (15)
output_file[256:384, 256:384] 	= image[128:256, 256:384].copy()		# 1,2 (7)  -> 2,2 (11)
output_file[128:256, 256:384] 	= image[128:256, 384:512].copy()		# 1,3 (8)  -> 1,2 (7)

output_file[0:128, 0:128] 		= image[256:384, 0:128].copy()			# 2,0 (9)  -> 0,0 (1)
output_file[128:256, 0:128] 	= image[256:384, 128:256].copy()		# 2,1 (10) -> 1,0 (5)
output_file[256:384, 384:512] 	= image[256:384, 256:384].copy()		# 2,2 (11) -> 2,3 (12)
output_file[128:256, 384:512] 	= image[256:384, 384:512].copy()		# 2,3 (12) -> 1,3 (8)

output_file[384:512, 128:256] 	= image[384:512, 0:128].copy()			# 3,0 (13) -> 3,1 (9) 
output_file[0:128, 384:512] 	= image[384:512, 128:256].copy()		# 3,1 (14) -> 0,3 (4) 
output_file[0:128, 128:256] 	= image[384:512, 256:384].copy()		# 3,2 (15) -> 0,1 (2)
output_file[256:384, 0:128] 	= image[384:512, 384:512].copy()		# 3,3 (16)-> 2,0 (14)

# show reshuffled image
cv2.imshow(windowName, output_file)
cv2.imwrite("output.jpg", output_file)
keypressed = cv2.waitKey(0)

cv2.destroyAllWindows()