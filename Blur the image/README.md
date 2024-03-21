# Image Blurring using OpenCV

This Python script demonstrates how to blur an image using the Gaussian blur technique with OpenCV library.

## Prerequisites

- Python 3.11
- OpenCV (cv2) library

## Installation

1. Clone this repository or download the script file directly.

2. Install the required dependencies using pip:
   
   ```bash
   pip install opencv-python



## Usage

1. Place the image you want to blur in the same directory as the script.
    
2. Run the script `blurred.py`.
    
3. The script will read the image, apply Gaussian blur with a specified kernel size, and save the blurred image as `blurred_image.jpg` in the same directory.

## Customization

You can adjust the blur effect by modifying the kernel size passed to the `cv.GaussianBlur` function. The larger the kernel size, the more pronounced the blur effect.

## Files

- `blurred.py`: Python script for blurring an image.
- `img.jpg`: Sample input image.
- `blurred_image.jpg`: Output image after applying Gaussian blur.

## Example
![Example 1](example.jpg)




## License

