import cv2
import numpy as np

image = cv2.imread("watch_scene.jpg")
template = cv2.imread("watch.jpg.png")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

w, h = gray_template.shape[::-1]

result = cv2.matchTemplate(gray_image, gray_template, cv2.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

cv2.rectangle(image, top_left, bottom_right, (0,255,0), 2)

# Resize output to 4:3 ratio
output = cv2.resize(image, (640,480))

cv2.imshow("Detected Watch", output)

cv2.waitKey(0)
cv2.destroyAllWindows()