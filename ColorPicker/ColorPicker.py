# Importing required libraries
import cv2
import numpy as np

# Create a blank image with white color
img = np.ones((700, 400, 3), np.uint8) * 255

# Create a window with the title 'Color Picker'
cv2.namedWindow('Color Picker')

# Define a function that does nothing, used for trackbar callback
def nothing(x):
    pass

# Create a trackbar named '0:Off/n1:On' with initial value 0 (Off) and maximum value 1 (On)
s = cv2.createTrackbar('0:Off/n1:On', 'Color Picker', 0, 1, nothing)

# Create trackbars for adjusting the color (Red, Green, Blue)
cv2.createTrackbar('R', 'Color Picker', 0, 255, nothing)
cv2.createTrackbar('G', 'Color Picker', 0, 255, nothing)
cv2.createTrackbar('B', 'Color Picker', 0, 255, nothing)

# Loop to continuously show the image and check for user input
while True:
    # Display the image in the window 'Color Picker'
    cv2.imshow('Color Picker', img)
    
    # Check for user input
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    # Get the current position of trackbars for Red, Green, and Blue channels
    r = cv2.getTrackbarPos('R', 'Color Picker')
    g = cv2.getTrackbarPos('G', 'Color Picker')
    b = cv2.getTrackbarPos('B', 'Color Picker')
    
    # Get the current position of the trackbar '0:Off/n1:On'
    s = cv2.getTrackbarPos('0:Off/n1:On', 'Color Picker')
    
    # If the '0:Off/n1:On' trackbar is ON (s = 1), set the color of the image to (r, g, b)
    if s == 0:
        pass
    else:
        img[:] = [r, g, b]
