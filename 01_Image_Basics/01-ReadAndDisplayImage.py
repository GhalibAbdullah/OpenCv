import cv2

# ---------- Step 1: Load the image ----------
image_path = r'../assets/example.png'  # Make sure this file exists in the directory
image = cv2.imread(image_path)

# ---------- Step 2: Validate image loading ----------
if image is None:
    print(f"Could not load image from {image_path}")
    exit()

print(f"Image loaded successfully.")
print(f"Original Dimensions: {image.shape}")  # Height, Width, Channels

# ---------- Step 3: Resize image to half its size ----------
resized_image = cv2.resize(image, (image.shape[1]//2, image.shape[0]//2))
print(f"Resized Dimensions: {resized_image.shape}")

# ---------- Step 4: Convert to grayscale ----------
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# ---------- Step 5: Display all versions ----------
cv2.imshow('Original Image', image)
cv2.imshow('Resized Image', resized_image)
cv2.imshow('Grayscale Image', gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
