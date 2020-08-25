import cv2
import numpy as np
import pyautogui

video = cv2.VideoCapture(0)
video.set(3, 640)     #id no 3 = width
video.set(4, 480)     #id no 4 = height
video.set(10, 100)    #id no 10 = brightness, we are changing brightness

lower_red = np.array([0,50,50])
upper_red = np.array([10,255,255])
lower_red1 = np.array([170,50,50])
upper_red1 = np.array([180,255,255])

centroid_x = 0
centroid_y = 0
cnt = 0
while True:
    success, img = video.read()
    img = cv2.flip(img, 1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #frame_threshed = cv2.inRange(hsv, red_min, red_max)
    mask0 = cv2.inRange(hsv, lower_red, upper_red)
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    mask = mask0+mask1
    contours, hierarchy = cv2.findContours(mask, 1, 2)
    max_area = 0
    if contours:
        for i in contours:
            area = cv2.contourArea(i)
            if area > max_area:
                max_area = area
                cnt = i
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        centroid_x = int((x + x + w) / 2)
        centroid_y = int((y + y + h) / 2)

    cv2.circle(img, (centroid_x, centroid_y), 2, (0, 0, 255), 2)
    #down
    cv2.line(img, (450, 260), (450, 360), (255, 0, 0), 4)
    cv2.line(img, (500, 260), (500, 360), (255, 0, 0), 4)
    cv2.line(img, (450, 360), (500, 360), (255, 0, 0), 4)
    #left
    cv2.line(img, (350, 260), (450, 260), (255, 0, 0), 4)
    cv2.line(img, (350, 210), (450, 210), (255, 0, 0), 4)
    cv2.line(img, (350, 260), (350, 210), (255, 0, 0), 4)
    #up
    cv2.line(img, (450, 210), (450, 110), (255, 0, 0), 4)
    cv2.line(img, (500, 210), (500, 110), (255, 0, 0), 4)
    cv2.line(img, (450, 110), (500, 110), (255, 0, 0), 4)
    #right
    cv2.line(img, (500, 260), (600, 260), (255, 0, 0), 4)
    cv2.line(img, (500, 210), (600, 210), (255, 0, 0), 4)
    cv2.line(img, (600, 260), (600, 210), (255, 0, 0), 4)

    if centroid_x > 450 and centroid_x < 500:
        if centroid_y >= 110 and centroid_y < 210:
            print("up")
            pyautogui.press('up')
        elif centroid_y > 260 and centroid_y <= 360:
            print("down")
            pyautogui.press('down')

    if centroid_y>=210 and centroid_y<=260:
        if centroid_x>=350 and centroid_x<450:
            print("left")
            pyautogui.press('left')
        elif centroid_x>500 and centroid_x<=600:
            print("right")
            pyautogui.press('right')

    cv2.imshow("Video", img)
    if cv2.waitKey(10) & 0xFF == ord('q'):         #to exit video press 'q'
        break