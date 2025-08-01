import cv2

# ---------- Step 1: Load the pre-trained Haar Cascade classifier ----------
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# ---------- Step 2: Load the image ----------
image_path = 'face_sample.jpg'  # Use a photo with one or more faces
img = cv2.imread(image_path)

if img is None:
    print(f"❌ Image not found: {image_path}")
    exit()

# ---------- Step 3: Convert image to grayscale ----------
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ---------- Step 4: Detect faces ----------
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

print(f"👥 Number of faces detected: {len(faces)}")

# ---------- Step 5: Draw rectangles around detected faces ----------
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# ---------- Step 6: Display result ----------
cv2.imshow("Face Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
