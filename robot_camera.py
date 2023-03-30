import cv2
url = "http://192.168.4.1/capture"

while True:
    cap = cv2.VideoCapture(url)
    if not cap.isOpened():
        print("Cap is not opened")
    ret, frame = cap.read()
    if not ret:
            break
    cv2.imshow('openCV Feed', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows
