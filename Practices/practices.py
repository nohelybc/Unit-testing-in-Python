# create a class that reads an image in an input and evaluates if it is a jpeg or png

import os
import sys
import cv2
import matplotlib.pyplot as plt


class ImageReader:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = cv2.imread(self.image_path)
        self.image_name = os.path.basename(self.image_path)
        self.image_extension = self.image_name.split('.')[-1]

    def get_image(self):
        return self.image

    def get_image_name(self):
        return self.image_name

    def get_image_extension(self):
        return self.image_extension

    def is_image(self):
        return self.image_extension in ['jpg', 'png']

    def show_image(self):
        plt.imshow(self.image)
        plt.show()

    def save_image(self, output_path):
        cv2.imwrite(output_path, self.image)

