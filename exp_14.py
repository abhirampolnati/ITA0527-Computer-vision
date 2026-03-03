import cv2
import numpy as np

# Read the image
image = cv2.imread("hulkbhai.jpg")

if image is None:
    print("Image not found")
else:
    rows, cols = image.shape[:2]

    # Source points (choose 4 points from the image)
    src_points = np.float32([
        [50, 50],
        [cols - 50, 40],
        [60, rows - 50],
        [cols - 40, rows - 40]
    ])

    # Destination points
    dst_points = np.float32([
        [0, 0],
        [cols, 0],
        [0, rows],
        [cols, rows]
    ])

    # Get perspective transformation matrix
    matrix = cv2.getPerspectiveTransform(src_points, dst_points)

    # Apply perspective transformation
    perspective_image = cv2.warpPerspective(image, matrix, (cols, rows))

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Perspective Transformed Image", perspective_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()