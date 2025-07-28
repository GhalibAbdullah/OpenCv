import cv2

# ---------- Step 1: Initialize webcam ----------
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Failed to open webcam.")
    exit()

# ---------- Step 2: Read the first frame and convert to gray ----------
ret, prev_frame = cap.read()
prev_frame = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
prev_frame = cv2.GaussianBlur(prev_frame, (21, 21), 0)

print("Motion detection started. Press 'q' to quit.")

while True:
    # Capture next frame
    ret, frame = cap.read()
    if not ret:
        break

    # Preprocess current frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # Compute absolute difference
    frame_delta = cv2.absdiff(prev_frame, gray)
    _, thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)

    # Dilate thresholded image to fill in holes
    thresh = cv2.dilate(thresh, None, iterations=2)

    # Find contours of movement
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 1000:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow("Live Feed", frame)
    cv2.imshow("Motion", thresh)

    prev_frame = gray.copy()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
