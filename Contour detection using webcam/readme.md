<h1 align="center">Contour detection using webcam</h1>
<p align="center">
  <img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg" alt="Made with Python">
  <img src="https://img.shields.io/badge/Made%20with-OpenCV-9cf.svg" alt="Made with OpenCV">
  <img src="https://img.shields.io/badge/Made%20with-Numpy-blue.svg" alt="Made with Numpy">


</p>
This Python script enables real-time color thresholding in the HSV color space using OpenCV. It utilizes trackbars to adjust the lower and upper HSV thresholds, allowing users to filter out specific colors from the webcam feed.

## Examples

<div align="center">
  <img src="https://github.com/Shawon5030/Computer-Vision/assets/149573785/152bd882-10a0-4eb1-9ace-678ac8563300" width="200" height="200">
  <img src="https://github.com/Shawon5030/Computer-Vision/assets/149573785/579ac9bf-b1c3-4f49-be2d-84cbbb82b708" width="200" height="200">

</div>
## Functionality Overview

1. **Webcam Capture:** The script captures frames from the webcam in real-time.
2. **Trackbars Creation:** Trackbars are created to adjust the lower and upper thresholds for HSV values.
3. **Color Thresholding:** The input frame is converted to the HSV color space, and a binary mask is created based on the specified HSV thresholds.
4. **Contour Detection:** Contours are detected in the thresholded image to identify shapes and objects.
5. **Visualization:** The original frame with contours drawn and the thresholded image are displayed in separate windows.
6. **User Interaction:** Users can adjust the trackbars in real-time to fine-tune the color filtering process.

This approach provides a simple yet effective means of visually isolating specific colors from an input image in real-time.

## How it Works

The script consists of a main loop that continuously reads frames from the webcam, processes them, and displays the results. Here's a simplified breakdown of the code:

```python
# Import required libraries
import cv2
import numpy as np

# Open webcam
cap = cv2.VideoCapture(0)

# Function to do nothing
def nothing(x):
    pass

# Create trackbars for adjusting threshold values
cv2.namedWindow('Color Adjustments', cv2.WINDOW_NORMAL)
cv2.createTrackbar('Thresh', 'Color Adjustments', 0, 255, nothing)
# Create trackbars for adjusting lower and upper HSV values
# ...

while cap.isOpened():
    # Read frame from the webcam
    b, frame = cap.read()

    # Preprocess frame: resize, convert to HSV
    # ...

    # Apply color thresholding
    # ...

    # Find contours and draw them
    # ...

    # Display images
    # ...

    # User interaction: press 'q' to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the webcam and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
<p>This approach provides a simple yet effective means of visually isolating specific colors from an input image in real-time.</p>


<h2 align="center">Author:</h2>
<h6 align="center">Mahmudul Haque Shawon:</h6>
<p align="center"><a href="https://www.linkedin.com/in/mahmudulhaque600/">Linkedin</a></p>
<p align="center"><a href="https://web.facebook.com/profile.php?id=100076803278386">Facebook</a></p>
<p align="center"><a href="haquemahmudul600@gmail.com">Gmail</a></p>
```
```

