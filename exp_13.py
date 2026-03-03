import cv2
import numpy as np

# Read the image
image = cv2.imread("hulkbhai.jpg")

if image is None:
    print("Image not found")
else:
    rows, cols = image.shape[:2]

    # Select 3 points in the original image
    src_points = np.float32([
        [0, 0],
        [cols - 1, 0],
        [0, rows - 1]
    ])

    # Define corresponding points in the output image
    dst_points = np.float32([
        [0, rows * 0.3],
        [cols * 0.85, rows * 0.25],
        [cols * 0.15, rows * 0.9]
    ])

    # Get affine transformation matrix
    matrix = cv2.getAffineTransform(src_points, dst_points)

    # Apply affine transformation
    affine_image = cv2.warpAffine(image, matrix, (cols, rows))

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Affine Transformed Image", affine_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()