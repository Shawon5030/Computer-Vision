# <h1 align="center">Motion Detection System using OpenCV, Mediapipe</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg" alt="Made with Python">
  <img src="https://img.shields.io/badge/Made%20with-OpenCV-9cf.svg" alt="Made with OpenCV">
  <img src="https://img.shields.io/badge/Made%20with-Numpy-blue.svg" alt="Made with Numpy">
  <img src="https://img.shields.io/badge/Made%20with-winsound-orange.svg" alt="Made with winsound">
</p>

## Overview

This project implements an enhanced motion detection system using OpenCV, Mediapipe, and Winsound in Python. It captures video frames from a webcam, analyzes the frames for motion, and alerts the user when motion is detected. This system can be used for various applications, including security monitoring, surveillance, and interactive installations.

### Features

- Real-time motion detection using OpenCV and Mediapipe.
- Alerts the user by drawing bounding boxes around moving objects and playing a sound.
- Adjustable sensitivity threshold for motion detection.
- Easy-to-use interface suitable for beginners and advanced users.

### How it Works

1. **Capturing Video Frames**: The system captures frames from the default webcam using OpenCV's `VideoCapture` class.
2. **Detecting Motion**: It calculates the absolute difference between consecutive frames to detect motion using OpenCV's `absdiff` function.
3. **Thresholding and Blurring**: The absolute difference image is converted to grayscale, thresholded to create a binary image, and then blurred using Gaussian blur to reduce noise.
4. **Finding Contours**: Contours are found in the binary image using OpenCV's `findContours` function.
5. **Drawing Bounding Boxes**: Bounding boxes are drawn around the detected contours to highlight moving objects.
6. **Alerting User**: If a contour's area exceeds a certain threshold, indicating significant motion, the system alerts the user by displaying "Thief" text above the bounding box and playing a sound using the `winsound` module.

### Requirements

- Python 3.x
- OpenCV
- Numpy
- winsound





### Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/shawon5030/Computer-Vision/new/main/Security%20cam.git


This project implements a motion detection system using OpenCV and Mediapipe in Python. It captures video frames from a webcam, analyzes the frames for motion, and alerts the user when motion is detected. This system can be used for various applications, including security monitoring, surveillance, and interactive installations.


<h2>Author:</h2>
<h6>Mahmudul Haque Shawon:</h6>
<p><a href="https://www.linkedin.com/in/mahmudulhaque600/">Linkedin</a></p>
<p><a href="https://web.facebook.com/profile.php?id=100076803278386">Facebook</a></p>
<p><a href="haquemahmudul600@gmail.com">Gmail</a></p>
