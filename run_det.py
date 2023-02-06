import cv2
import matplotlib.pyplot as plt
import urllib.request
import numpy as np
import concurrent.futures

url = "http://192.168.4.1/Test"

cv2.namedWindow("Live transmission", cv2.WINDOW_AUTOSIZE)
while True:
        img_resp=urllib.request.urlopen(url)
        imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
        im = cv2.imdecode(imgnp,-1)
        cv2.imshow('live transmission',im)
        key=cv2.waitKey(5)
        if key==ord('q'):
            break
            
cv2.destroyAllWindows()