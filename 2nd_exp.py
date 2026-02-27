import cv2

# Read the image
image = cv2.imread("hulkbhai.jpg")

if image is None:
    print("Image not found")
else:
    # Apply Gaussian Blur
    blur_image = cv2.GaussianBlur(image, (7, 7), 0)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Gaussian Blurred Image", blur_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()