import streamlit as st
import numpy as np
import cv2 as cv
from PIL import Image

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)

    img = Image.open(picture)
    img = img.save("img.jpg")

    im = cv.imread("img.jpg")
    img_gray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(img_gray, 150, 255, cv.THRESH_BINARY)
    st.image(img_gray, caption='Image with Contours')
