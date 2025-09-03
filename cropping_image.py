import cv2  # Import the OpenCV library

image = cv2.imread("photo/avengers.jpg")

cropped_image = image[0:100, 0:100]

# Show the cropped image
cv2.imshow('Cropped Image', cropped_image)

cv2.waitKey(0)
cv2.destroyAllWindows()