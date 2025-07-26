import cv2

# ---------- Step 1: Load two images of the same size ----------
img1 = cv2.imread('../assets/blend1.jpg')  # e.g., landscape
img2 = cv2.imread('../assets/blend2.jpg')  # e.g., cityscape

if img1 is None or img2 is None:
    print("❌ One or both images could not be loaded.")
    exit()

# Resize both images to the same dimensions if needed
img1 = cv2.resize(img1, (600, 400))
img2 = cv2.resize(img2, (600, 400))

# ---------- Step 2: Blend images ----------
alpha = 0.6  # weight of img1
beta = 1.0 - alpha  # weight of img2

blended = cv2.addWeighted(img1, alpha, img2, beta, 0)

# ---------- Step 3: Show result ----------
cv2.imshow("Image 1", img1)
cv2.imshow("Image 2", img2)
cv2.imshow("Blended Image", blended)

cv2.waitKey(0)
cv2.destroyAllWindows()
