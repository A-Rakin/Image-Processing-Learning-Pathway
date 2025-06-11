# Import the OpenCV library
import cv2

# Load the Haar Cascade classifier for face detection from the specified XML file
faceCascade = cv2.CascadeClassifier("Haar_Cascade_File/haarcascade_frontalface_default.xml")

# Open the default webcam (device index 0)
cap = cv2.VideoCapture(0)

# Start an infinite loop to continuously capture frames from the webcam
while True:
    video, img = cap.read()  # Read a frame from the webcam
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert the frame to grayscale (face detection works better on grayscale images)

    # Detect faces in the grayscale image
    # Parameters:
    #   1.1 = scaleFactor: Specifies how much the image size is reduced at each image scale
    #   4 = minNeighbors: Specifies how many neighbors each candidate rectangle should have to retain it
    faces = faceCascade.detectMultiScale(gray, 1.1, 4)

    # Loop over the detected faces and draw rectangles around them
    for (x, y, w, h) in faces:
        # Draw a blue rectangle (BGR: 255,0,0) around each detected face
        # (x, y) is the top-left corner; (x+w, y+h) is the bottom-right corner
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Show the frame with face rectangles in a window titled "img"
    cv2.imshow("img", img)

    # Wait for 30 milliseconds for a key press
    # If the ESC key (ASCII 27) is pressed, exit the loop
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

# Release the webcam resource and close all OpenCV windows after breaking the loop
cap.release()
cv2.destroyAllWindows()
