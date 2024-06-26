

<h1 align="center">Real-time HSV Color Thresholding using OpenCV</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg" alt="Made with Python">
  <img src="https://img.shields.io/badge/Made%20with-OpenCV-9cf.svg" alt="Made with OpenCV">
  <img src="https://img.shields.io/badge/Made%20with-Numpy-blue.svg" alt="Made with Numpy">
</p>

This Python script enables real-time color thresholding in the HSV color space using OpenCV. Users can interactively adjust lower and upper HSV thresholds using trackbars to filter out specific colors from an input image.


## Examples

<div align="center">
  <img src="https://github.com/Shawon5030/Computer-Vision/assets/149573785/94fe8ff4-e2c3-4725-af55-0bda514ac7fe" width="200" height="200">
  <img src="https://github.com/Shawon5030/Computer-Vision/assets/149573785/d9a3b633-063f-4836-971b-f8951cc1f03c" width="200" height="200">
  <img src="https://github.com/Shawon5030/Computer-Vision/assets/149573785/cf6907c8-8216-4faa-85f8-649a692bc164" width="200" height="200">
  <img src="https://github.com/Shawon5030/Computer-Vision/assets/149573785/57cc3e3e-c93b-488f-ae22-0b0e4725c55d" width="200" height="200">
</div>

## How it Works

The script utilizes the OpenCV library to perform real-time color thresholding in the HSV (Hue, Saturation, Value) color space. For a detailed explanation, refer to the [How it Works](#how-it-works) section in the code repository.

## Requirements

- Python 3.x
- OpenCV
- Numpy

## Installation





<h2>How it Works</h2>
<p>The script utilizes the OpenCV library to perform real-time color thresholding in the HSV (Hue, Saturation, Value) color space. Here's a step-by-step explanation of its functionality:</p>

<ol>
  <li><strong>Input Image:</strong> The script reads an input image from the file system.</li>
  
  <li><strong>Trackbars Creation:</strong> It creates trackbars for adjusting the lower and upper thresholds of the HSV color space. These trackbars allow users to dynamically adjust the filtering criteria for isolating specific colors.</li>
  
  <li><strong>HSV Conversion:</strong> The input image is converted from the BGR color space to the HSV color space using the <code>cv2.cvtColor()</code> function. This conversion is necessary because the HSV color space is more suitable for color thresholding tasks.</li>
  
  <li><strong>Thresholding:</strong> The script continuously updates the HSV image, mask, and resulting image based on the threshold values adjusted using the trackbars. It uses the <code>cv2.inRange()</code> function to create a binary mask that isolates pixels within the specified HSV range.</li>
  
  <li><strong>Bitwise AND Operation:</strong> The binary mask obtained from thresholding is applied to the original input image using the <code>cv2.bitwise_and()</code> function. This operation retains only those pixels from the original image that fall within the specified HSV range, effectively filtering out unwanted colors.</li>
  
  <li><strong>Real-time Visualization:</strong> Throughout the process, the script displays the HSV image, mask, and resulting image in separate windows using <code>cv2.imshow()</code>. Users can observe the effects of adjusting the trackbars in real-time.</li>
  
  <li><strong>User Interaction:</strong> The script waits for the user to press the 'q' key to exit the loop and terminate the program. This allows users to adjust the thresholds until they achieve the desired color segmentation.</li>
</ol>

<p>This approach provides a simple yet effective means of visually isolating specific colors from an input image in real-time.</p>


<h2>Author:</h2>
<h6>Mahmudul Haque Shawon:</h6>
<p><a href="https://www.linkedin.com/in/mahmudulhaque600/">Linkedin</a></p>
<p><a href="https://web.facebook.com/profile.php?id=100076803278386">Facebook</a></p>
<p><a href="haquemahmudul600@gmail.com">Gmail</a></p>
