import cv2
import numpy as np

# Get image size from user
width = int(input("Enter image width: "))
height = int(input("Enter image height: "))

# Create white image
img = np.ones((height, width, 3), dtype=np.uint8) * 255

# Circle parameters
center = (width//2, height//2)   # center of image
radius = min(width, height)//4   # radius
color = (255, 0, 0)              # Blue color
thickness = 3                    # circle border thickness

# Draw circle
cv2.circle(img, center, radius, color, thickness)

# Display image
cv2.imshow("Circle Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()