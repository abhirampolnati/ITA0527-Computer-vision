import cv2

# Read the image
image = cv2.imread("hulkbhai.jpg")

if image is None:
    print("Image not found")
else:
    # Rotate image 90 degrees clockwise
    rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("90 Degree Clockwise Rotated Image", rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()