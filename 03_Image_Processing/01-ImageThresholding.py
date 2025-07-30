import cv2
import numpy as np

# ---------- Step 1: Load the image in grayscale ----------
image_path = '../assets/example.png'
gray_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if gray_img is None:
    print(f"Failed to load image: {image_path}")
    exit()

# ---------- Step 2: Apply different thresholding techniques ----------

# 1. Binary Threshold
_, thresh_binary = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)

# 2. Binary Inverted
_, thresh_binary_inv = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY_INV)

# 3. Truncate Threshold
_, thresh_trunc = cv2.threshold(gray_img, 127, 255, cv2.THRESH_TRUNC)

# 4. To Zero Threshold
_, thresh_tozero = cv2.threshold(gray_img, 127, 255, cv2.THRESH_TOZERO)

# 5. To Zero Inverted
_, thresh_tozero_inv = cv2.threshold(gray_img, 127, 255, cv2.THRESH_TOZERO_INV)

# ---------- Step 3: Display the images ----------
cv2.imshow("Original Grayscale", gray_img)
cv2.imshow("Threshold Binary", thresh_binary)
cv2.imshow("Threshold Binary INV", thresh_binary_inv)
cv2.imshow("Threshold Trunc", thresh_trunc)
cv2.imshow("Threshold ToZero", thresh_tozero)
cv2.imshow("Threshold ToZero INV", thresh_tozero_inv)

cv2.waitKey(0)
cv2.destroyAllWindows()
