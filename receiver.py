from mlsocket import MLSocket
import cv2
from _thread import *
import numpy as np
import time
threadCount = 0

HOST = '128.199.16.74'
#HOST = '127.0.0.1'
PORT = 4590

s = MLSocket()
s.connect((HOST, PORT))

def show(i, j):
	j = str(j)

	while True:
		cv2.imshow(j, i)
		key = cv2.waitKey(1)
		if key == 27:
			break
	cv2.destroyAllWindows()


while True:
	data = s.recv(1024)
	threadCount += 1
	start_new_thread(show, (data,threadCount))
    
    




