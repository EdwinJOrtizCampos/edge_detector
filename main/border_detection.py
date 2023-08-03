import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def img_treatment(path):

    # Read image and apply pre-processing
    input = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)
    grays = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grays, (5,5), 0)

    # Calculate edges and create overlay
    edges = cv2.Canny(blur,100,200)
    edges = np.repeat(edges[:, :, np.newaxis], 3, axis=2)
    blur2 = cv2.GaussianBlur(edges, (3,3), 0)

    # Apply overlay and show result
    result = np.concatenate((input, input + blur2), axis=1)

    plt.imshow(result)
    plt.title("Original | Results")
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    path = "edge_detector/main/images"
    for file in os.listdir(path):
        img_treatment(f"{path}/{file}")
