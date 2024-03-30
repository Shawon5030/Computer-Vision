import cv2  # Importing the OpenCV library for computer vision tasks.
import mediapipe as mp  # Importing the Mediapipe library for various AI solutions, including face detection.

video = cv2.VideoCapture(0)  # Opening a connection to the default camera (index 0) for capturing video you can us 1,2 also

while video.isOpened():  # Looping over the video capture until it's open.
    b, frame = video.read()  # Reading the next frame from the video capture.
    if b == True:  # Checking if the frame was successfully read.
        
        frame = cv2.resize(frame, (700, 400))  # Resizing the frame to a specific width and height.
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Converting the color space of the frame from BGR to RGB.
    
        result = mp.solutions.face_detection.FaceDetection().process(rgb)  # Using Mediapipe for face detection on the frame.
        draw = mp.solutions.drawing_utils  # Importing drawing utilities from Mediapipe.
    
        if result is not None and result.detections is not None:  # Checking if faces were detected.
            
            for i in result.detections:  # Looping over each detected face.
                draw.draw_detection(frame, i)  # Drawing bounding boxes around the detected faces.
            cv2.imshow('Real Time Face Detection', frame)  # Displaying the frame with face detections.
            
        if cv2.waitKey(25) & 0xff == ord('q'):  # Waiting for a key press for 25 seconds and checking if it's 'q' to exit the loop.
            break
    else:  # If reading the frame was unsuccessful, exit the loop.
        break

video.release()  # Releasing the video capture resource.
cv2.destroyAllWindows()  # Closing all OpenCV windows.