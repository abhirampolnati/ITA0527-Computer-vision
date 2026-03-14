import cv2
import numpy as np

# Create white image
img = np.ones((400, 600, 3), dtype=np.uint8) * 255

# Get text from user
text = input("Enter text to display on image: ")

# Text properties
position = (100, 200)
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
color = (0, 0, 255)   # Red color
thickness = 2

# Put text on image
cv2.putText(img, text, position, font, font_scale, color, thickness)

# Show image
cv2.imshow("Text on Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()