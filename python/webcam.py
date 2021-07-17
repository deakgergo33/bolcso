import time
import datetime
import cv2

cam = cv2.VideoCapture(0)

i = 0

print(datetime.datetime.now().time())

while i<10: 
    ret, frame = cam.read()
    i+=1

cam.close()

print(datetime.datetime.now().time())

cam.release()

