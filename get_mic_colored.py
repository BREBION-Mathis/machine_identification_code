import cv2
import numpy as np
import sys

if len(sys.argv) != 3:
    print("Usage: python get_mic_colored.py <input_image> <output_image>")
    sys.exit(1)

# Image uploading
image_path = sys.argv [1]
output_path = sys.argv [2]
image = cv2.imread(image_path)

# Convert image to HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Set color ranges for yellow dots (in HSV space)
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])

# Apply mask to detect yellow dots
mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

# Find the outlines of the yellow dots
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw rectangles around the yellow dots
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imwrite(output_path, image)
