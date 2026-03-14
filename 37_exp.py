import cv2
import numpy as np

# Read image
img = cv2.imread("pk.jpg")

# Convert to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define color range (example: detect red color foreground)
lower = np.array([0, 30, 60])
upper = np.array([20, 150, 255])

# Create mask for selected color
mask = cv2.inRange(hsv, lower, upper)

# Extract foreground using mask
foreground = cv2.bitwise_and(img, img, mask=mask)

# Show images
cv2.imshow("Original Image", img)
cv2.imshow("Mask", mask)
cv2.imshow("Foreground Image", foreground)

cv2.waitKey(0)
cv2.destroyAllWindows()