import cv2

# Load grayscale image
img1 = cv2.imread(r'images.jpeg', 0)  # 0 for grayscale
if img1 is None:
    print("Error: Image not found or could not be loaded!")
    exit()

print(img1)  # Print matrix of the image
cv2.imshow('Grayscale Image', img1)  # Show grayscale image
cv2.waitKey(0)
cv2.destroyAllWindows()

# Load color image
img2 = cv2.imread(r'images.jpeg', 1)  # 1 for color
if img2 is None:
    print("Error: Image not found or could not be loaded!")
    exit()

print(img2)  # Print matrix of the image

# Save the image
status = cv2.imwrite('bike.jpeg', img2)
print("Image saved:", status)  # Prints True if image is saved successfully

# Get properties of the image
dimensions = img2.shape
height = img2.shape[0]
width = img2.shape[1]
channels = img2.shape[2]  # Now this works because the image is in color
size1 = img2.size

print("Dimensions:", dimensions)
print("Height:", height)
print("Width:", width)
print("Channels:", channels)
print("Size in bytes:", size1)

# Split channels
b, g, r = cv2.split(img2)

# Merge and display channels
cv2.imshow('Original Image', img2)
cv2.imshow('Blue Channel', b)   # Blue channel grayscale
cv2.imshow('Green Channel', g)  # Green channel grayscale
cv2.imshow('Red Channel', r)    # Red channel grayscale

cv2.waitKey(0)
cv2.destroyAllWindows()

# Resize image
new_width = 270
new_height = 400
dim = (new_width, new_height)
resized = cv2.resize(img2, dim, interpolation=cv2.INTER_AREA)

print("Resized Image Shape:", resized.shape)

# Display resized image
cv2.imshow('Original Image', img2)
cv2.imshow('Resized Image', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
