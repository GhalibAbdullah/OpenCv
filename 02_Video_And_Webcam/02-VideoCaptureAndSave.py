import cv2

# ---------- Step 1: Open webcam ----------
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Unable to open webcam.")
    exit()

# ---------- Step 2: Define video codec and create VideoWriter ----------
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = 20.0

# Define the codec and output file name
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # You can also use 'MJPG', 'X264'
out = cv2.VideoWriter('output.avi', fourcc, fps, (frame_width, frame_height))

print("Recording... Press 'q' to stop.")

# ---------- Step 3: Read and write video frames ----------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame (optional)
    frame = cv2.flip(frame, 1)

    # Write the frame to file
    out.write(frame)

    # Display the recording frame
    cv2.imshow('Recording...', frame)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Saved video as 'output.avi'")
        break

# ---------- Step 4: Release everything ----------
cap.release()
out.release()
cv2.destroyAllWindows()
