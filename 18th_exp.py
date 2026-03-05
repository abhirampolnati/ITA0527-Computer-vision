import cv2

# Read the image
image = cv2.imread("hulkbhai.jpg")

if image is None:
    print("Image not found")
else:
    # Display original image
    original = image.copy()

    # Define ROI (Crop area)
    # Format: image[y1:y2, x1:x2]
    roi = image[100:300, 150:350]

    # Copy ROI
    roi_copy = roi.copy()

    # Paste ROI at a new location
    image[50:250, 50:250] = roi_copy

    # Display images
    cv2.imshow("Original Image", original)
    cv2.imshow("ROI Cropped", roi)
    cv2.imshow("Image after Pasting ROI", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()