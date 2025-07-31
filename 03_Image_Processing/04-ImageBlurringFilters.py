import cv2

# ---------- Step 1: Load the image ----------
image_path = '../assets/example.jpg'
img = cv2.imread(image_path)

if img is None:
    print(f"Image not found: {image_path}")
    exit()

# ---------- Step 2: Apply various blurring techniques ----------

# 1. Averaging Blur
blur_avg = cv2.blur(img, (5, 5))

# 2. Gaussian Blur
blur_gaussian = cv2.GaussianBlur(img, (5, 5), 0)

# 3. Median Blur
blur_median = cv2.medianBlur(img, 5)

# 4. Bilateral Filter (preserves edges while blurring)
blur_bilateral = cv2.bilateralFilter(img, 9, 75, 75)

# ---------- Step 3: Show all versions ----------
cv2.imshow("Original", img)
cv2.imshow("Averaging Blur", blur_avg)
cv2.imshow("Gaussian Blur", blur_gaussian)
cv2.imshow("Median Blur", blur_median)
cv2.imshow("Bilateral Filter", blur_bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()
