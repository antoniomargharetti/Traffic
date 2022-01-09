import cv2
import numpy as np
import os
import sys
import tensorflow as tf

IMG_WIDTH = 30
IMG_HEIGHT = 30

def load_data(data_dir):
    """
    Load image data from directory `data_dir`.

    Assume `data_dir` has one directory named after each category, numbered
    0 through NUM_CATEGORIES - 1. Inside each category directory will be some
    number of image files.

    Return tuple `(images, labels)`. `images` should be a list of all
    of the images in the data directory, where each image is formatted as a
    numpy ndarray with dimensions IMG_WIDTH x IMG_HEIGHT x 3. `labels` should
    be a list of integer labels, representing the categories for each of the
    corresponding `images`.
    """
    images = []
    labels = []
    for i in range(43):
        location = os.path.join(data_dir, str(i))
        for filename in os.listdir(location):
            image = cv2.imread(os.path.join(location, filename))
            image = cv2.resize(image, (IMG_WIDTH, IMG_HEIGHT))
            images.append(image)
            labels.append(i)
    return images, labels



flula = load_data("gtsrb")
print(type(flula))