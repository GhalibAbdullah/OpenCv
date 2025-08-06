import cv2
import numpy as np

# ---------- Step 1: Load the image ----------
image_path = 'example.jpg'
img = cv2.imread(image_path)

if img is None:
    print(f"❌ Image not found: {image_path}")
    exit()

# ---------- Step 2: Create a black mask ----------
mask = np.zeros(img.shape[:2], dtype="uint8")  # single channel mask (grayscale)

# Draw a white filled rectangle on the mask (region to keep)
cv2.rectangle(mask, (100, 100), (300, 300), 255, -1)

# ---------- Step 3: Apply mask using bitwise AND ----------
masked_img = cv2.bitwise_and(img, img, mask=mask)

# ---------- Step 4: Show results ----------
cv2.imshow("Original Image", img)
cv2.imshow("Mask", mask)
cv2.imshow("Masked Result", masked_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
