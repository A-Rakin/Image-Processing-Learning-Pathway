import cv2  # Import the OpenCV library for image processing

img = cv2.imread("photo/avengers.jpg")  # Read the image from the specified path and store it in the variable 'img'

cv2.imshow("Output",img)  # Display the image in a window titled "Output"

cv2.waitKey(0)  # Wait indefinitely for a key press before closing the window
