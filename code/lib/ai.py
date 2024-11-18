import numpy as np
import cv2


cv2.startWindowThread()

video = cv2.VideoCapture(0)

while True:

    rect, frame = video.read()

    cv2.imshow('frame', frame)
