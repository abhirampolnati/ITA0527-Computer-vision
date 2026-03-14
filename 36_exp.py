import cv2

# Read image
img = cv2.imread("car.jpg")

# Create background subtractor
bg = cv2.createBackgroundSubtractorMOG2()

# Apply background subtraction
fgmask = bg.apply(img)

# Show original image
cv2.imshow("Original Image", img)

# Show background subtracted image
cv2.imshow("Background Subtracted Image", fgmask)

cv2.waitKey(0)
cv2.destroyAllWindows()