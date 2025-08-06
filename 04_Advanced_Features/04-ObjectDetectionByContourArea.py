import cv2

# ---------- Step 1: Load image ----------
image_path = 'objects.jpg'  # Use an image with multiple distinct shapes
img = cv2.imread(image_path)

if img is None:
    print(f"❌ Failed to load image: {image_path}")
    exit()

# ---------- Step 2: Convert to grayscale and threshold ----------
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# ---------- Step 3: Find contours ----------
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# ---------- Step 4: Filter contours by area and draw ----------
output = img.copy()
min_area = 1000  # Minimum area of object to be considered

for contour in contours:
    area = cv2.contourArea(contour)
    if area > min_area:
        cv2.drawContours(output, [contour], -1, (0, 255, 0), 2)
        print(f"🧱 Object with area: {int(area)}")

# ---------- Step 5: Show results ----------
cv2.imshow("Original", img)
cv2.imshow("Binary", binary)
cv2.imshow("Detected Objects", output)

cv2.waitKey(0)
cv2.destroyAllWindows()
