'''
AUTHOR: ceposerio@up.edu.ph
DESC: a demo of background subtraction with a series of images as input
'''

import numpy as np 
import cv2

# the higher, the better (?)
__NUM_LEARN_FRAMES__ = 200
__FOREGROUND_DIFF_THRESH__ = 25

cap = cv2.VideoCapture(0)

# gets __NUM_LEARN_FRAMES__, and its median to compute for the background.
print("Learning the background frames. Please wait...")
background_frames = []
while len(background_frames) < __NUM_LEARN_FRAMES__:
	ret, frame = cap.read()
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	background_frames.append(frame)

background_frames = np.array(background_frames)
background = np.median(background_frames, axis = 0)

backgroundShow = background.clip(0,255).astype('uint8')
print("Done!")
cv2.imshow("background", backgroundShow)

# loop until 'q' is pressed.
while(1):
	ret, current_frame = cap.read()
	current_gray_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)

	diff = current_gray_frame - background
	diff = np.absolute(diff)
	mask = diff > __FOREGROUND_DIFF_THRESH__
	foreground = current_frame.copy()
	mask2 = np.invert(mask)
	foreground[mask2] = [255,255,255]
	output = np.concatenate((current_frame, foreground), axis=1).astype('uint8')
	cv2.imshow("Output", output)

	key = cv2.waitKey(10) & 0xFF
	if key == ord('q'): break

cap.release()
cv2.destroyAllWindows()

