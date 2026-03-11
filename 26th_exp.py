import cv2

# Read video
cap = cv2.VideoCapture("plane.mp4")

frames = []

# Store all frames
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

cap.release()

# Reverse frames
frames.reverse()

# Get video properties
height, width, layers = frames[0].shape
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("reverse_video.avi", fourcc, 30, (width, height))

# Write reversed frames
for frame in frames:
    out.write(frame)
    cv2.imshow("Reversed Video", frame)
    cv2.waitKey(30)

out.release()
cv2.destroyAllWindows()