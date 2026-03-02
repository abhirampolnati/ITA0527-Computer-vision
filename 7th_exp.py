import cv2

cap = cv2.VideoCapture("jyothiba.mp4")

if not cap.isOpened():
    print("Video not found")
    exit()

# 4:3 resolution
WIDTH = 640
HEIGHT = 480

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize frame to 4:3
    frame_43 = cv2.resize(frame, (WIDTH, HEIGHT))

    cv2.imshow("Video (4:3 Ratio)", frame_43)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()