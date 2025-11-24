import cv2
import copy
import numpy as np

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
        
        if any(edges):
            self.processedImage = edges
            return True
        return False
    
    def getLineData(self):
        """Puts all line-related information in the variables"""
        
        # Save a deepcopy of the processed image
        image = copy.deepcopy(self.processedImage)
        
        # Reasign the main variable to an empty list
        self.processedImage = []
        
        # Get image dimensions
        height, width, _ = image.shape
        x = width // 3
        
        # Split image into 3 parts
        self.processedImage[0] = image[:, :x]
        self.processedImage[1] = image[:, x:2*x]
        self.processedImage[2] = image[:, 2*x:width]
        
        self.left = True if len(cv2.HoughLines(self.processedImage[0], 1, np.pi/180, 200)) >= 1 else None
        self.front = True if  len(cv2.HoughLines(self.processedImage[1], 1, np.pi/180, 200)) >= 1 else None
        self.right = True if len(cv2.HoughLines(self.processedImage[2], 1, np.pi/180, 200)) >= 1 else None
