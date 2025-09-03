import cv2  # Import the OpenCV library
image = cv2.imread("photo/avengers.jpg")

cropped_image = image[0:100, 0:100]

resized_image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)


# Save the cropped and resized images
cv2.imwrite('cropped_image.jpg', cropped_image)
cv2.imwrite('resized_image.jpg', resized_image)

print('Images have been saved successfully.')

