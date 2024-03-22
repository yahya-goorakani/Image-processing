import cv2 as cv
def blurred():
    image = cv.imread('img.jpg')

    if image is None:
        print("Error: Unable to load image.")
    else:   
        blurred_image = cv.GaussianBlur(image, (65, 65), 0)

        cv.imwrite('blurred_image.jpg', blurred_image)

if __name__ == "__main__":

    blurred()
