import cv2
import glob

cascade = cv2.CascadeClassifier("haarcascade.xml")
image = cv2.imread('a8.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

rects = cascade.detectMultiScale(
gray,
scaleFactor=1.1,
minNeighbors=5,
minSize=(30, 30),
flags=cv2.cv.CV_HAAR_SCALE_IMAGE
)

if len(rects) > 0:
        for (x, y, w, h) in rects:
            blurImg = cv2.blur(image,(200,200)) 
            print "Image scan result: Alert, Nudity Content Found"
            cv2.namedWindow('blurred image',cv2.WINDOW_NORMAL)
            cv2.resizeWindow('blurred image', 600,600)
            cv2.imshow('blurred image',blurImg)

else:

                print "Image scan result: No Nudity Content Found"
                cv2.imshow("Rects not found", image)

cv2.waitKey(0)
cv2.destroyAllWindows()