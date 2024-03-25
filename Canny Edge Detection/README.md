# Image Processing with OpenCV

This Python script demonstrates basic image processing using the OpenCV library. The script performs the following operations on an input image:

1. Read an image from a file.
2. Convert the image to grayscale.
3. Apply Gaussian blur to the grayscale image.
4. Perform edge detection using the Canny edge detector.


## Prerequisites

- Python 3.11
- OpenCV
- NumPy
- Matplotlib

## Installation

You can install the required packages using pip:

    ```bash
    pip install opencv-python numpy matplotlib


## Usage

1. Replace 'path_to_your_image.jpg' with the path to the image you want to process.
2. Run the script.


## Parameters

 - cv2.Canny(blurred_image, 50, 150):
 - blurred_image: The input grayscale image.
 - 50: Lower threshold for the hysteresis procedure.
 - 150: Upper threshold for the hysteresis procedure.
 - You can adjust these thresholds according to your specific requirements to get better edge detection results.

