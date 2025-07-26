import cv2
import numpy as np

# ---------- Step 1: Load the image ----------
image_path = '../assets/example.png'
img = cv2.imread(image_path)

if img is None:
    print(f"❌ Failed to load image: {image_path}")
    exit()

# ---------- Step 2: Convert to grayscale and apply median blur ----------
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_blur = cv2.medianBlur(gray, 7)

# ---------- Step 3: Detect edges using adaptive threshold ----------
edges = cv2.adaptiveThreshold(
    gray_blur, 255,
    cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY,
    blockSize=9,
    C=9
)

# ---------- Step 4: Apply bilateral filter for cartoon effect ----------
color = cv2.bilateralFilter(img, d=9, sigmaColor=250, sigmaSpace=250)

# ---------- Step 5: Combine edges with smoothed color ----------
cartoon = cv2.bitwise_and(color, color, mask=edges)

# ---------- Step 6: Display results ----------
cv2.imshow("Original", img)
cv2.imshow("Edges", edges)
cv2.imshow("Cartoon", cartoon)

cv2.waitKey(0)
cv2.destroyAllWindows()
