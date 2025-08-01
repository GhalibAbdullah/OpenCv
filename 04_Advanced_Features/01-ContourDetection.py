import cv2

# ---------- Step 1: Load image and convert to grayscale ----------
image_path = 'example.jpg'
image = cv2.imread(image_path)

if image is None:
    print(f"❌ Failed to load image: {image_path}")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# ---------- Step 2: Apply binary thresholding ----------
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# ---------- Step 3: Find contours ----------
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# ---------- Step 4: Draw contours on a copy ----------
image_with_contours = image.copy()
cv2.drawContours(image_with_contours, contours, -1, (0, 255, 0), 2)

# ---------- Step 5: Display the results ----------
print(f"🔍 Number of contours detected: {len(contours)}")
cv2.imshow("Original", image)
cv2.imshow("Binary", binary)
cv2.imshow("Contours", image_with_contours)

cv2.waitKey(0)
cv2.destroyAllWindows()
