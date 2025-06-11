import cv2  # Import the OpenCV library

img = cv2.imread("photo/avengers.jpg")  # Load the image from the specified path

ImgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert the original image from BGR color to grayscale

ImgBlur = cv2.GaussianBlur(ImgGrey,(99,99), 0) ## Apply a Gaussian blur to the grayscale image using a 99x99 kernel; sigmaX is set to 0 (auto-calculated)

cv2.imshow("Output in Grey Image", ImgGrey)  # Display the grayscale image in a window

cv2.imshow("Output in Original Image", img)  # Display the original color image in a separate window

cv2.imshow("Output in Blur Image", ImgBlur) # Display the Blur image in a separate window

cv2.waitKey(0)  # Wait indefinitely until a key is pressed
