import cv2 as cv
import numpy as np

def mask():
    image = cv.imread('img.jpg')
    if image is None:
        print(" Error:Enabl to load file. ")
    else:
        hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
        #green color
        lower = np.array([36,25,25])
        upper = np.array([86, 255,255])

        mask = cv.inRange(hsv, lower, upper)
        color_only = cv.bitwise_and(image, image, mask = mask)
        mask = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)
        cv.imwrite("only_color.jpg",color_only)
        return  cv.imwrite("threshold_mask.jpg",cv.subtract(image, mask))
if __name__ == "__main__" :
  
 mask()