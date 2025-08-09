import cv2
import numpy as np

# ---------- Step 1: Create a blank canvas ----------
canvas = np.zeros((300, 512, 3), dtype=np.uint8)
cv2.namedWindow("Color Picker")

# ---------- Step 2: Create callback (does nothing) ----------
def nothing(x):
    pass

# ---------- Step 3: Create RGB trackbars ----------
cv2.createTrackbar("R", "Color Picker", 0, 255, nothing)
cv2.createTrackbar("G", "Color Picker", 0, 255, nothing)
cv2.createTrackbar("B", "Color Picker", 0, 255, nothing)

# ---------- Step 4: Live update loop ----------
print("🎨 Adjust the sliders to change the background color. Press ESC to exit.")

while True:
    # Get current positions
    r = cv2.getTrackbarPos("R", "Color Picker")
    g = cv2.getTrackbarPos("G", "Color Picker")
    b = cv2.getTrackbarPos("B", "Color Picker")

    # Update canvas color
    canvas[:] = [b, g, r]

    cv2.imshow("Color Picker", canvas)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC key
        break

cv2.destroyAllWindows()
