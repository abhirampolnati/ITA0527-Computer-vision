import cv2
import numpy as np

width = int(input("Enter image width: "))
height = int(input("Enter image height: "))

# Create white image
image = np.ones((height, width, 3), dtype=np.uint8) * 255

# Box size
box_w = width // 10
box_h = height // 10

# Draw colored boxes
image[0:box_h, 0:box_w] = (0,0,0)              # Black
image[0:box_h, width-box_w:width] = (255,0,0)  # Blue
image[height-box_h:height, 0:box_w] = (0,255,0)# Green
image[height-box_h:height, width-box_w:width] = (0,0,255) # Red

# Show image
cv2.namedWindow("Output Image", cv2.WINDOW_NORMAL)
cv2.imshow("Output Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()