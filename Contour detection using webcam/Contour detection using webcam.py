import cv2  # Import OpenCV library
import numpy as np  # Import NumPy library for numerical operations

# Open webcam
cap = cv2.VideoCapture(0)

# Function to do nothing
def nothing(x):
     pass

# Create a window named 'Color Adjustments'
cv2.namedWindow('Color Adjustments', cv2.WINDOW_NORMAL)
# Resize the window
cv2.resizeWindow('Color Adjustments',300,300)

# Create trackbars for adjusting threshold values
cv2.createTrackbar('Thresh','Color Adjustments',0,255,nothing)

# Create trackbars for adjusting lower and upper HSV values
cv2.createTrackbar('lh','Color Adjustments',0,255,nothing)
cv2.createTrackbar('ls','Color Adjustments',0,255,nothing)
cv2.createTrackbar('lv','Color Adjustments',0,255,nothing)

cv2.createTrackbar('hh','Color Adjustments',255,255,nothing)
cv2.createTrackbar('hs','Color Adjustments',255,255,nothing)
cv2.createTrackbar('hv','Color Adjustments',255,255,nothing)

# Main loop for processing video frames
while cap.isOpened():
     # Read frame from the webcam
     b, frame = cap.read()
     
     # Resize the frame
     frame = cv2.resize(frame, (300,300))

     # Get current trackbar positions
     lh = cv2.getTrackbarPos('lh','Color Adjustments')
     ls = cv2.getTrackbarPos('ls','Color Adjustments')
     lv = cv2.getTrackbarPos('lv','Color Adjustments')

     hh = cv2.getTrackbarPos('hh','Color Adjustments')
     hs = cv2.getTrackbarPos('hs','Color Adjustments')
     hv = cv2.getTrackbarPos('hv','Color Adjustments')

     # Get threshold value
     thres = cv2.getTrackbarPos('Thresh' , 'Color Adjustments')

     # Define lower and upper HSV values
     lower = np.array([lh, ls, lv])
     upper = np.array([hh, hs, hv])

     # Convert frame to HSV color space
     hsv = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)

     # Create a mask using inRange function
     mask = cv2.inRange(hsv , lower,upper)

     # Apply threshold to the mask
     b , t = cv2.threshold(mask,thres,255,cv2.THRESH_BINARY_INV)

     # Find contours in the thresholded image
     cnt , h = cv2.findContours(t,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

     # Draw contours and convex hulls on the frame
     for i in cnt:
         epslion =.0001*cv2.arcLength(i,True)
         data = cv2.approxPolyDP(i ,epslion,True )
         hull = cv2.convexHull(data)

         cv2.drawContours(frame , [i],-1,(0,0,255),1)
         cv2.drawContours(frame , [hull],-1,(0,0,255),1)
         
         # Display thresholded image
         cv2.imshow('thresh',t)
         
         # Display frame with contours
         cv2.imshow('frame',frame)

     # Check for 'q' key press to exit the loop
     if cv2.waitKey(25) & 0xff == ord('q'):
         # Save thresholded image
         cv2.imwrite('E:\Mahmudul\Image Processing\Practice/32 - Contour detection using webcam.py/thresh.png',t)
         # Save frame with contours
         cv2.imwrite('E:\Mahmudul\Image Processing\Practice/32 - Contour detection using webcam.py/frame.png',frame)
         break
     
# Release the webcam and destroy all OpenCV windows
cap.release()
cv2.destroyAllWindows()
