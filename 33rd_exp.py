import cv2
import numpy as np

# Get size from user
width = int(input("Enter image width: "))
height = int(input("Enter image height: "))

# Create white image
img = np.ones((height, width, 3), dtype=np.uint8) * 255

# Draw rectangle
start_point = (50, 50)
end_point = (width-50, height-50)
color = (0, 0, 255)   # Red color
thickness = 3

cv2.rectangle(img, start_point, end_point, color, thickness)

# Display image
cv2.imshow("Rectangle Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()