import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Read an image from a file
image_path = 'img.jpg'
image = cv2.imread(image_path)

# Check if the image is loaded successfully
if image is None:
    print("Error: Could not open or read the image.")
    exit()

# Step 2: Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Apply Gaussian blur to the grayscale image
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Step 4: Perform edge detection using Canny edge detector
edges = cv2.Canny(blurred_image, 50, 150)

# Display the original image, grayscale image, and edge-detected image
titles = ['Original Image', 'Grayscale Image', 'Edge-detected Image']
images = [cv2.cvtColor(image, cv2.COLOR_BGR2RGB), gray_image, edges]

for i in range(3):
    plt.subplot(1, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.axis('off')

plt.show()
