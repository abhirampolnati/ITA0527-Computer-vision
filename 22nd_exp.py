import cv2
import numpy as np

# Read the image
image = cv2.imread("hulkbhai.jpg")

if image is None:
    print("Image not found")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Create kernel
    kernel = np.ones((5,5), np.uint8)

    # Apply Closing operation
    closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Closing Operation", closing)

    cv2.waitKey(0)
    cv2.destroyAllWindows()