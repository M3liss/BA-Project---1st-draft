import cv2
import numpy as np
vid_capture = cv2.VideoCapture(0)
while True:
        #capture frame by frame
        ret, frame = vid_capture.read()
        if not ret:
            print("Cannot receive frame. Make sure no other application is using the camera.")
            break
        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rows = img_gray.shape[0]
        det_balls = cv2.HoughCircles(img_gray, cv2.HOUGH_GRADIENT, 1, rows / 8, param1=50, param2=30, minRadius=1, maxRadius=30)
        if det_balls is not None:
            circles = np.uint16(np.around(det_balls))
            for i in circles[0, :]:
                center = (i[0], i[1])
                radius = i[2]
                cv2.circle(img_gray, center, radius, (255, 0, 255), 3)
        cv2.imshow("Grayscale", img_gray)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

vid_capture.release()
cv2.destroyAllWindows
