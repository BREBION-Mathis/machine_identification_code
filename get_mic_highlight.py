import sys
import cv2
import numpy as np

def highlight_yellow_dots(input_path, output_path):
    image = cv2.imread(input_path)
    
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([40, 255, 255])
    
    yellow_mask = cv2.inRange(hsv_image, lower_yellow, upper_yellow)
    
    yellow_dots = cv2.bitwise_and(image, image, mask=yellow_mask)
    
    cv2.imwrite(output_path, yellow_dots)

if len(sys.argv) != 3:
    print("Usage: python monscript.py input_image output_image")
    sys.exit(1)

input_image_path = sys.argv[1]
output_image_path = sys.argv[2]

highlight_yellow_dots(input_image_path, output_image_path)
