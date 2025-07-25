import cv2
import numpy as np

# ---------- Step 1: Create a blank white canvas ----------
canvas = np.ones((600, 600, 3), dtype="uint8") * 255

# ---------- Step 2: Draw basic shapes ----------
cv2.rectangle(canvas, (50, 50), (200, 200), (255, 0, 0), 2)      # Blue rectangle
cv2.circle(canvas, (400, 150), 75, (0, 255, 0), -1)              # Green filled circle
cv2.line(canvas, (0, 0), (600, 600), (0, 0, 255), 4)             # Red diagonal line

# ---------- Step 3: Draw ellipse ----------
cv2.ellipse(canvas, (300, 400), (100, 50), 0, 0, 360, (255, 165, 0), 2)  # Orange ellipse

# ---------- Step 4: Draw a polygon ----------
pts = np.array([[250, 500], [300, 450], [350, 500], [300, 550]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(canvas, [pts], isClosed=True, color=(128, 0, 128), thickness=2)

# ---------- Step 5: Add multiple lines of text ----------
cv2.putText(canvas, 'OpenCV Drawing Demo', (120, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
cv2.putText(canvas, 'Shapes: Rectangle, Circle, Line, Ellipse, Polygon', (40, 580), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (50, 50, 50), 1)

# ---------- Step 6: Display result ----------
cv2.imshow('Drawing Canvas', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
