import cv2

# Read the image
image = cv2.imread("pk.jpg")

if image is None:
    print("Image not found")
else:
    # Copy original image
    watermarked = image.copy()

    # Watermark details
    text = "abhi_polnati"
    position = (30, image.shape[0] - 30)

    font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX  # NEW FONT
    font_scale = 1.2
    color = (255, 255, 255)  # White
    thickness = 2

    # Add watermark
    cv2.putText(
        watermarked,
        text,
        position,
        font,
        font_scale,
        color,
        thickness,
        cv2.LINE_AA
    )

    # Display
    cv2.imshow("Original Image", image)
    cv2.imshow("Watermarked Image", watermarked)

    cv2.waitKey(0)
    cv2.destroyAllWindows()