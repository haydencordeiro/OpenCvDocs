

# read image
import numpy as np
import cv2
# LOAD AN IMAGE USING 'IMREAD'
img = cv2.imread("Resources/lena.png")
# DISPLAY
cv2.imshow("Lena Soderberg", img)
cv2.waitKey(0)


# Read Video
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture("Resources/test_ video.mp4")
while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow("Result", img)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break


# Read from webcam
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)
while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break


# basic funtions

img = cv2.imread("Resources/lena.png")
kernel = np.ones((5, 5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
imgCanny = cv2.Canny(img, 150, 200)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)
