# Image Edge Detection using Python and OpenCV

This Python code provides a simple script for performing image edge detection using OpenCV. It reads images from a specified directory, applies preprocessing steps, detects edges using the Canny algorithm, and then creates an overlay of the original image with the detected edges. The resulting image is displayed using Matplotlib.

## Prerequisites
Before running the code, ensure you have the following libraries installed:
- OpenCV (`cv2`)
- NumPy (`numpy`)
- Matplotlib (`matplotlib`)

You can install these libraries using `pip`:

```bash
pip install -r requirements.txt
```

## How to use the code
1. Download the Python script or copy the code into a new Python file (e.g., `image_edge_detection.py`).

2. Place your images in a directory and set the `path` variable in the `__main__` block to the path of that directory or place the desired images on the `/images` folder. The script will loop through all the images in the specified directory and apply edge detection to each image.

3. Run the script using the following command:

```bash
python image_edge_detection.py
```

## Code Explanation
1. The code imports the necessary libraries: `cv2` for image processing, `numpy` for array operations, `matplotlib.pyplot` for displaying images, and `os` for directory handling.

2. The `img_treatment` function takes the path of an image as input and performs the following steps:
   - Read the image from the specified path using OpenCV (`cv2.imread`) and convert the color space from BGR to RGB.
   - Convert the RGB image to grayscale (`cv2.cvtColor`) for edge detection.
   - Apply Gaussian blurring (`cv2.GaussianBlur`) to the grayscale image to reduce noise.
   - Use the Canny edge detection algorithm (`cv2.Canny`) to find edges in the blurred grayscale image.
   - Convert the 1-channel edge image to a 3-channel image using `numpy.repeat`, so it can be overlaid on the original RGB image.
   - Apply Gaussian blurring again to the 3-channel edge image for better visualization.
   - Concatenate the original image and the overlay image horizontally using `numpy.concatenate`.

3. The `__main__` block executes when the script is run directly. It sets the `path` variable to the directory containing the images. The script then loops through each file in the directory, calls the `img_treatment` function on each image, and displays the results.

4. After running the script, a window will pop up showing the original image on the left and the result with overlaid edges on the right. Close the window to proceed to the next image.

## Notes
- The code assumes that the input images are in RGB format. If your images are already in grayscale or other formats, you may need to adjust the code accordingly.
- The threshold values (100 and 200) used for Canny edge detection can be modified based on the images and the desired edge detection results. Experiment with different values to achieve the best results for your specific images.
- You can specify `blur_amount` (affects mask thickness) & `color` (edge color) when calling the script.

This is a little project I made to kill some time and learn more about Python. All credit goes to the creators of the libraries required to run this script.
