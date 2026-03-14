import cv2

cap = cv2.VideoCapture("plane.mp4")

frames = []

# Read all frames
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

cap.release()

# Play video in reverse slow motion
for frame in reversed(frames):

    # Resize frame to 4:3 ratio
    frame = cv2.resize(frame, (640, 480))   # 640x480 is 4:3

    cv2.imshow("Reverse Slow Motion 4:3", frame)

    if cv2.waitKey(100) & 0xFF == 27:   # 100 ms delay = slow motion
        break

cv2.destroyAllWindows()