import cv2

# Read image
image = cv2.imread("face.jpg")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load smile cascade
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")

# Detect smiles
smiles = smile_cascade.detectMultiScale(gray, 1.8, 20)

# Draw rectangles around detected smiles
for (x, y, w, h) in smiles:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0,255,0), 2)

# Display result
cv2.imshow("Smile Detection", image)

cv2.waitKey(0)
cv2.destroyAllWindows()