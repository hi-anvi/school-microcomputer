import cv2
import copy
import numpy as np
from pyzbar import pyzbar

def splitImage(origImage):
    """Returns a list which splits the image in 3 equal pieces"""

    # Make deepcopy of the original image
    image = copy.deepcopy(origImage)

    # Calculate the one-third width of the image
    height, width = image.shape
    x = width // 3

    # Split image into 3 parts- left, middle, right
    left_img  = image[:, :x]
    mid_img   = image[:, x:2*x]
    right_img = image[:, 2*x:]

    return [left_img, mid_img, right_img]

class Line():
    def __init__ (self, image):
        self.image = image
        self.front = True
        self.midRight = None
        self.midLeft = None
        self.right = None
        self.left = None
        self.processedImage = None
    
    def processImage(self):
        """Detect line"""
        
        # Convert the img to grayscale
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        # Apply edge detection method on the image
        edges = cv2.Canny(gray, 50, 150, apertureSize=3)
        
        if np.any(edges):
            self.processedImage = edges
            return True
        return False

    def getLineData(self):
        """Puts all line-related information in the variables"""

        # Update the variable
        self.processedImage = splitImage(self.processedImage)

        def detect(img):
            lines = cv2.HoughLines(img, 1, np.pi/180, 200)
            return lines is not None and len(lines) > 0

        # According to the images, check for the lines
        self.left  = detect(self.processedImage[0])
        self.front = detect(self.processedImage[1])
        self.right = detect(self.processedImage[2])

    def checkForFork(self):
        """Checks for a fork in the line"""

        count = 0

        if self.left:
            count += 1
        if self.right:
            count += 1
        if self.front:
            count += 1
        
        if count > 1:
            return True
        return False

    def QRCodeCheck(self, classroom):
        """If there is a fork in the road, run QR detection"""

        if not checkForFork():
            return None

        # Update the variable
        self.image = splitImage(self.image)

        # Convert to grey for better detection
        gray_left = cv2.cvtColor(self.image[0], cv2.COLOR_BGR2GRAY)
        gray_mid = cv2.cvtColor(self.image[1], cv2.COLOR_BGR2GRAY)
        gray_right = cv2.cvtColor(self.image[2], cv2.COLOR_BGR2GRAY)

        # Detect code
        code_left = pyzbar.decode(gray_left)
        code_mid = pyzbar.decode(gray_mid)
        code_right = pyzbar.decode(gray_right)

        # Check for classroom
        for obj in code_left:
            data_str = obj.data.decode("utf-8")
            classes = data_str.split(",")
            if classroom in classes:
                self.right = None
                self.left = True
                self.front = None
                return None

        for obj in code_mid:
            data_str = obj.data.decode("utf-8")
            classes = data_str.split(",")
            if classroom in classes:
                self.right = None
                self.left = None
                self.front = True
                return None

        for obj in code_right:
            data_str = obj.data.decode("utf-8")
            classes = data_str.split(",")
            if classroom in classes:
                self.right = True
                self.left = None
                self.front = None
                return None