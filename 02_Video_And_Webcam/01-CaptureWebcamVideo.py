import cv2
import time

# ---------- Step 1: Initialize webcam ----------
cap = cv2.VideoCapture(0)  # 0 is the default camera index

# Check if camera opened successfully
if not cap.isOpened():
    print("Could not access the webcam.")
    exit()

print("Webcam accessed successfully. Press 'q' to quit.")

# ---------- Step 2: Set resolution (optional) ----------
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# ---------- Step 3: Real-time capture loop ----------
prev_time = time.time()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame.")
        break

    # Flip the frame horizontally (like a mirror)
    frame = cv2.flip(frame, 1)

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Add FPS counter
    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time
    cv2.putText(frame, f"FPS: {int(fps)}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display both original and grayscale side by side
    cv2.imshow('Webcam - Original', frame)
    cv2.imshow('Webcam - Grayscale', gray)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("🔚 Exiting webcam feed.")
        break

# ---------- Step 4: Release resources ----------
cap.release()
cv2.destroyAllWindows()
