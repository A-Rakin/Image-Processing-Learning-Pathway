import cv2  # Import the OpenCV library

image = cv2.imread("photo/avengers.jpg")

resized_image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)

# Show the resized image
cv2.imshow('Resized Image', resized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()


