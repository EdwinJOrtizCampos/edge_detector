import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def img_treatment(path, blur_amount = (3,3), color = [255, 0, 0]):

    # Read image and apply pre-processing
    image = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)
    grays = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grays, (5,5), 0)

    # Calculate edges and create overlay
    edges = cv2.Canny(blur, 100, 200)
    edges = np.repeat(edges[:, :, np.newaxis], 3, axis=2)
    edge_blur = cv2.GaussianBlur(edges, blur_amount, 0)

    # Apply overlay to a copy of the input image
    image_masked = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)
    color = np.array(color)
    edge_blur_coordinates = np.column_stack(np.where(edge_blur > 0))
    image_masked[edge_blur_coordinates[:, 0], edge_blur_coordinates[:, 1]] = color

    # Show input/output comparison using Matplotlib
    result = np.concatenate((image, image_masked), axis=1)
    plt.imshow(result)
    plt.title("Original | Results")
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    path = "edge_detector/main/images"
    for file in os.listdir(path):
        img_treatment(f"{path}/{file}", (1,1), [0, 255, 0])
