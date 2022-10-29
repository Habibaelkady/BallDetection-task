import cv2
import imutils
redLower =  (0,50,120)
redUpper = (10,255,255)
yellowLower = (25,70,120)
yellowUpper = (30,255,255)
blueLower= (90,60,0)
blueUpper= (122,255,255)
test1="C:\\Users\\Judge\\Downloads\\ball_086.jpg"
test2="C:\\Users\\Judge\\Downloads\\ball_083.jpg"
test3="C:\\Users\\Judge\\Downloads\\ball_082.jpg"
frame = cv2.imread(test2)
frame=cv2.resize(frame,[int(frame.shape[1]*0.3),int(frame.shape[0]*0.3)])
blurred = cv2.GaussianBlur(frame, (11, 11), 0)
width, height = frame.shape[:2]
hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
maskR = cv2.inRange(hsv, redLower, redUpper)
maskR = cv2.erode(maskR, None, iterations=2)
maskR = cv2.dilate(maskR, None, iterations=2)
cntsR = cv2.findContours(maskR.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)
cntsR = imutils.grab_contours(cntsR)
centerR = None
maskY = cv2.inRange(hsv, yellowLower, yellowUpper)
maskY = cv2.erode(maskY, None, iterations=2)
maskY = cv2.dilate(maskY, None, iterations=2)
cntsY = cv2.findContours(maskY.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)
cntsY = imutils.grab_contours(cntsY)
centerY = None
maskB= cv2.inRange(hsv, blueLower, blueUpper)
maskB = cv2.erode(maskB, None, iterations=2)
maskB = cv2.dilate(maskB, None, iterations=2)
cntsB = cv2.findContours(maskB.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)
cntsB = imutils.grab_contours(cntsB)
centerB = None

if len(cntsR) > 10:
    c1 = max(cntsR, key=cv2.contourArea)
    ((xr, yr), radiusR) = cv2.minEnclosingCircle(c1)
    M = cv2.moments(c1)
    centerR = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        # To see the centroid clearly
    if radiusR > 7:
        cv2.circle(frame, (int(xr), int(yr)), int(radiusR), (0, 0, 0), 5)
        cv2.imwrite("circled_frame.png", cv2.resize(frame, (int(height / 2), int(width / 2))))
        cv2.circle(frame, centerR, 5, (0, 0, 255), -1)
if len(cntsY) > 0:
    c2 = max(cntsY, key=cv2.contourArea)
    ((xy, yy), radiusY) = cv2.minEnclosingCircle(c2)
    M = cv2.moments(c2)
    centerY = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        # To see the centroid clearly
    if radiusY > 7:
        cv2.circle(frame, (int(xy), int(yy)), int(radiusY), (0, 0, 0), 5)
        cv2.imwrite("circled_frame.png", cv2.resize(frame, (int(height / 2), int(width / 2))))
        cv2.circle(frame, centerY, 5, (0, 0, 255), -1)
if len(cntsB) > 0:
    c3 = max(cntsB, key=cv2.contourArea)
    ((xb, yb), radiusB) = cv2.minEnclosingCircle(c3)
    M = cv2.moments(c3)
    centerY = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        # To see the centroid clearly
    if radiusB > 7:
        cv2.circle(frame, (int(xb), int(yb)), int(radiusB), (0, 0, 0), 5)
        cv2.imwrite("circled_frame.png", cv2.resize(frame, (int(height / 2), int(width / 2))))
        cv2.circle(frame, centerY, 5, (0, 0, 255), -1) #center

cv2.imshow("Frame", frame)
cv2.waitKey(0)
