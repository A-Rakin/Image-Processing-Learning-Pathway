import cv2  # Import the OpenCV library

image = cv2.imread("photo/avengers.jpg")

cropped_image = image[0:100, 0:100]

# Show the cropped image
cv2.imshow('Cropped Image', cropped_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

"""
Step-by-Step Breakdown:
Cropping the Image:

OpenCV stores images as NumPy arrays, and cropping is achieved by slicing the array.

The code image[0:100, 0:100] selects the pixel rows from 0 to 100 and columns from 0 to 100, resulting in a 100x100 cropped image.

Displaying the Cropped Image:

The cropped portion of the image is displayed using the cv2.imshow() function, similar to how the full image was displayed earlier.

Closing the Window:

As before, cv2.waitKey(0) waits for a key press and cv2.destroyAllWindows() closes the window.

"""