from PIL import Image, ImageDraw, ImageFont #library to play around images in python
img = Image.open("./Generate_Certificate/Certificate_Template.jpg")

import matplotlib.pyplot as plt #To plot the image and know the coordinates
import numpy as np

def print_img(img):
    plt.imshow(np.array(img))
    plt.show()

import cv2 #library for image processing

img = cv2.imread("./Generate_Certificate/Certificate_Template.jpg")

def generate_certificate(img, name="Enter Name"):
    generate_image = img.copy()
    font = cv2.FONT_HERSHEY_DUPLEX
    coordinates = (700,780) # know these coordinate using matplotlib
    font_size = 3.5
    font_color = (51,51,51)
    font_thickness = 10
    cv2.putText(generate_image,name, coordinates, font, font_size, font_color, font_thickness) # keep it in same format or google
    return generate_image # because automaticaly saved in generated_image

def save_img(img, name):
    path = "./Generate_Certificate/Certi_{}.jpg".format(name)
    print(cv2.imwrite(path,img))

name = input("Enter the name you want on certificate: ")
generated_image = generate_certificate(img, name)
save_img(generated_image, name)