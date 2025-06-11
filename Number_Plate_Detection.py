# Import required libraries
import cv2  # OpenCV for image processing
import numpy as np  # NumPy for numerical operations
import pytesseract  # Tesseract OCR for text recognition
import imutils  # imutils for image resizing and convenience functions

# Set the path to the Tesseract OCR executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load the image from file
image = cv2.imread("photo/car5.jpg")

# Resize the image to width 500 while maintaining aspect ratio
image = imutils.resize(image, width=500)

# Convert the image to grayscale (required for edge detection and filtering)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a bilateral filter to remove noise while keeping edges sharp
gray = cv2.bilateralFilter(gray, 11, 17, 17)

# Use the Canny edge detector to find edges in the image
edge = cv2.Canny(gray, 170, 200)

# Find contours from the edge-detected image
cnts, new = cv2.findContours(edge.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# Make a copy of the original image for contour drawing
image1 = image.copy()
cv2.drawContours(image1, cnts, -1, (0, 225, 0), 3)  # Draw all contours in green

# Sort contours based on area (largest to smallest) and keep top 30
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:30]

# Variable to store the final number plate contour
NumberPlateCount = None

# Another copy of the image to draw top 30 contours
image2 = image.copy()
cv2.drawContours(image2, cnts, -1, (0, 255, 0), 3)

# Loop over contours to find one that looks like a license plate (a rectangle)
name = 1
for i in cnts:
    perimeter = cv2.arcLength(i, True)  # Calculate the perimeter
    approx = cv2.approxPolyDP(i, 0.02 * perimeter, True)  # Approximate the contour shape

    if len(approx) == 4:  # License plates are usually rectangular (4 sides)
        NumberPlateCount = approx  # Save the contour
        x, y, w, h = cv2.boundingRect(i)  # Get bounding box coordinates
        crp_img = image[y:y+h, x:x+w]  # Crop the license plate region
        cv2.imwrite(str(name) + '.png', crp_img)  # Save cropped image to file
        name += 1
        break  # Stop after finding the first possible license plate

# Draw the detected license plate contour on the original image
cv2.drawContours(image, [NumberPlateCount], -1, (0, 255, 0), 3)

# Load the cropped image and display it
crp_img_loc = '1.jpg'
cv2.imshow("Cropped Image", cv2.imread(crp_img_loc))

# Perform OCR (text recognition) on the cropped image using Tesseract
text = pytesseract.image_to_string(crp_img_loc, lang='eng')
print("Number is : NU 19 PL8 ", text)  # Print the recognized text (with a label)

# Display various image windows
cv2.imshow('original image', image)
# cv2.imshow('Gray Image', gray)  # Optional: View grayscale version
# cv2.imshow('Smoother', gray)    # Optional: View filtered image
# cv2.imshow("canny image", edge)  # Optional: View edge-detected image
# cv2.imshow("Canny after contours", image1)  # Optional: View all contours
# cv2.imshow("Top 30 contours", image2)       # Optional: View top 30 contours

cv2.imshow("Final Image", image)  # Show the final output with rectangle on license plate

# Wait indefinitely for a key press to close all windows
cv2.waitKey(0)
