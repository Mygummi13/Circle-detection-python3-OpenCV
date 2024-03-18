import cv2
import numpy as np
import matplotlib.pyplot as plt
import time


cap = cv2.VideoCapture(0) # Set Capture Device, in case of a USB Webcam try 1, or give -1 to get a list of available devices

try:
    while True:
        time.sleep(0.1) #Change time gap
        ret, frame = cap.read()

        if ret:
            gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            blur_image = cv2.GaussianBlur(gray_image, (9, 9), 2)
            circles = cv2.HoughCircles(blur_image, cv2.HOUGH_GRADIENT, dp=1.2, minDist=50,
                                       param1=50, param2=30, minRadius=20, maxRadius=55)

            if circles is not None:
                circles = np.round(circles[0, :]).astype("int")

                for (x, y, r) in circles:
                    cv2.circle(frame, (x, y), r, (0, 255, 0), 4)
                    cv2.rectangle(frame, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
                    print(f"Circle detected: Center=({x}, {y}), Radius={r}")
            cv2.imshow('Detected Circles', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            print("Failed to capture image")
            break

finally:
    cap.release()
    cv2.destroyAllWindows()
