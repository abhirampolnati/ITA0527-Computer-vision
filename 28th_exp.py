import cv2

vehicle_cascade = cv2.CascadeClassifier(
"C:\\Users\\abhir\\OneDrive\\Desktop\\computer_vision\\cars.xml"
)

cap = cv2.VideoCapture("traffic.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    vehicles = vehicle_cascade.detectMultiScale(gray, 1.1, 3)

    for (x, y, w, h) in vehicles:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

    cv2.imshow("Vehicle Detection", frame)

    if cv2.waitKey(30) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()