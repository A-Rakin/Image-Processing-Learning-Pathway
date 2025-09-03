import cv2  # Import the OpenCV library

image = cv2.imread("photo/avengers.jpg")

resized_image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)

# Show the resized image
cv2.imshow('Resized Image', resized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()


"""
Step-by-Step Breakdown:
Resizing the Image:

The cv2.resize() function is used to resize the image.

Setting (0, 0) for the size and using the fx=0.5 and fy=0.5 parameters scale the width and height by 50%, effectively resizing the image to half its original size.

Displaying the Resized Image:

The resized image is displayed in a new window using cv2.imshow(), just as the original image was displayed.

Closing the Window:

The window is closed using cv2.waitKey(0) and cv2.destroyAllWindows().

"""