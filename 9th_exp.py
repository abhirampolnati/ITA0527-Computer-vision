import cv2

# Read the image
image = cv2.imread("pk.jpg")

if image is None:
    print("Image not found")
else:
    # Original dimensions
    height, width = image.shape[:2]

    # Scale up (bigger image)
    bigger = cv2.resize(image, (int(width * 1.5), int(height * 1.5)))

    # Scale down (smaller image)
    smaller = cv2.resize(image, (int(width * 0.5), int(height * 0.5)))

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Bigger Image (Scaled Up)", bigger)
    cv2.imshow("Smaller Image (Scaled Down)", smaller)

    cv2.waitKey(0)
    cv2.destroyAllWindows()