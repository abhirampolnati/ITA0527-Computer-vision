import cv2
import numpy as np
from matplotlib import pyplot as plt

def analyze_color_histogram(image_path):
    # Read the image
    image = cv2.imread(image_path)

    if image is None:
        print("Image not found")
        return

    # Split into B, G, R channels
    b, g, r = cv2.split(image)

    # Calculate histograms
    hist_b = cv2.calcHist([b], [0], None, [256], [0, 256])
    hist_g = cv2.calcHist([g], [0], None, [256], [0, 256])
    hist_r = cv2.calcHist([r], [0], None, [256], [0, 256])

    # Plot histograms
    plt.figure()
    plt.title("Color Histogram Analysis")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Number of Pixels")

    plt.plot(hist_b, color='b', label='Blue')
    plt.plot(hist_g, color='g', label='Green')
    plt.plot(hist_r, color='r', label='Red')

    plt.legend()
    plt.show()

# Function call
analyze_color_histogram("pk.jpg")