import cv2

# ---------- Step 1: Load the image ----------
image_path = '../assets/example.png'
img = cv2.imread(image_path)

if img is None:
    print(f"Could not load image: {image_path}")
    exit()

# ---------- Step 2: Convert to different color spaces ----------

# 1. Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2. HSV (Hue, Saturation, Value)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 3. LAB color space
lab = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)

# ---------- Step 3: Display each version ----------
cv2.imshow("Original (BGR)", img)
cv2.imshow("Grayscale", gray)
cv2.imshow("HSV", hsv)
cv2.imshow("LAB", lab)

cv2.waitKey(0)
cv2.destroyAllWindows()
