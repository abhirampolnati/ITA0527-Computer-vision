import cv2
import numpy as np

# Read image
image = cv2.imread("pk.jpg")

if image is None:
    print("Image not found")
else:
    # Keep a copy of original image
    original = image.copy()

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)

    # Harris Corner Detection
    corners = cv2.cornerHarris(gray, 2, 3, 0.04)
    corners = cv2.dilate(corners, None)

    # Draw corners on image
    image[corners > 0.01 * corners.max()] = [0, 0, 255]

    # Display
    cv2.imshow("Original Image", original)
    cv2.imshow("Harris Corner Detection", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()