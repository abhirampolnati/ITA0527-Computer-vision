import cv2
import pytesseract

# Correct Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Open video
cap = cv2.VideoCapture("video1.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize to 4:3
    frame = cv2.resize(frame, (640,480))

    # Convert to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Extract text
    text = pytesseract.image_to_string(gray)

    print("Detected Text:", text)

    cv2.imshow("Video", frame)

    if cv2.waitKey(30) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()