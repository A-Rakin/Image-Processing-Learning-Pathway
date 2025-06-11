import cv2  # Import the OpenCV library


cap = cv2.VideoCapture("video/snowfall.mp4")  # Open the video file for reading

while True:  # Start an infinite loop to read and display video frames

    video, img = cap.read()  # Read the next frame from the video; 'video' is a boolean indicating success, 'img' is the frame

    if not video:
        break  # Stop if no frame is returned (end of video or error)

    cv2.imshow("Video", img)  # Display the current frame in a window titled "Video"

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Wait 1 ms for a key press; if 'q' is pressed, break the loop
        break

cap.release()  # Free the video capture object
cv2.destroyAllWindows()  # Close all OpenCV windows