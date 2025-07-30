import cv2

# ---------- Step 1: Load the image ----------
image_path = '../assets/example.png'
img = cv2.imread(image_path)

if img is None:
    print(f"Image not found: {image_path}")
    exit()

# ---------- Step 2: Convert image to grayscale ----------
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ---------- Step 3: Apply Gaussian Blur ----------
# Helps remove noise before edge detection
blurred = cv2.GaussianBlur(gray, (5, 5), 1.4)

# ---------- Step 4: Apply Canny edge detector ----------
# Thresholds: lower (minVal), upper (maxVal)
edges = cv2.Canny(blurred, 50, 150)

# ---------- Step 5: Display results ----------
cv2.imshow("Original Image", img)
cv2.imshow("Grayscale", gray)
cv2.imshow("Blurred", blurred)
cv2.imshow("Canny Edge Detection", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
