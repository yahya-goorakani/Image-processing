import cv2 as cv 
def unshpar():
    image = cv.imread('img.jpg')
    if image is None:
      print(" Error:Enable to load file. ")
    else:
      gaussian = cv.GaussianBlur(image, (0, 0), 2.0)
      return cv.imwrite('unshapr_image.jpg',cv.addWeighted(image, 2.2, gaussian, -1.0, 0))

if __name__ == "__main__":
      
    unshpar()
    
    
    
