<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Real-time Contour Detection using Webcam</title>
</head>
<body>
    <h1>Real-time Contour Detection using Webcam</h1>
    <p>This Python script demonstrates real-time contour detection using a webcam. It utilizes OpenCV for video capture and image processing.</p>

    <h2>Requirements</h2>
    <ul>
        <li>Python</li>
        <li>OpenCV</li>
        <li>NumPy</li>
    </ul>

    <h2>Usage</h2>
    <ol>
        <li>Clone the repository.</li>
        <li>Make sure you have Python installed on your system.</li>
        <li>Install the required libraries using pip:</li>
    </ol>

    <pre><code>pip install opencv-python numpy</code></pre>

    <ol start="4">
        <li>Run the script using the following command:</li>
    </ol>

    <pre><code>python contour_detection.py</code></pre>

    <p>Adjust the trackbars to manipulate the HSV values and threshold for contour detection.</p>

    <h2>Description</h2>
    <ul>
        <li>The script captures frames from the webcam and processes them for contour detection.</li>
        <li>Trackbars are provided for adjusting the lower and upper HSV values, as well as the threshold for contour detection.</li>
        <li>Contours and convex hulls are drawn on the frame in real-time based on the detected objects.</li>
    </ul>

    <h2>License</h2>
    <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
</body>
</html>

