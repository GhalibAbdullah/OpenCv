import cv2
import numpy as np

# ---------- Step 1: Setup canvas and variables ----------
canvas = np.ones((600, 800, 3), dtype="uint8") * 255
drawing = False
ix, iy = -1, -1

# ---------- Step 2: Define the mouse callback ----------
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            temp = canvas.copy()
            cv2.rectangle(temp, (ix, iy), (x, y), (0, 255, 0), 2)
            cv2.imshow("Drawing App", temp)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(canvas, (ix, iy), (x, y), (0, 255, 0), 2)

# ---------- Step 3: Create the window and bind the function ----------
cv2.namedWindow("Drawing App")
cv2.setMouseCallback("Drawing App", draw_rectangle)

# ---------- Step 4: Event loop ----------
print("🖱️ Drag your mouse to draw rectangles. Press ESC to exit.")
while True:
    cv2.imshow("Drawing App", canvas)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC key
        break

cv2.destroyAllWindows()
