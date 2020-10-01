import time
import numpy as nm
import pytesseract
import cv2
from PIL import ImageGrab
from playsound import playsound


def image_to_string():
    pytesseract.pytesseract.tesseract_cmd ="C:\Program Files (x86)\Tesseract-OCR\\tesseract.exe"

    while(True):

       cap = ImageGrab.grab(bbox=(700,300,1400,900))

       image_to_text = pytesseract.image_to_string(cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY),lang="eng")
       
       print(image_to_text)

       if "was The lmpostor" in image_to_text:
           playsound("wegothim.mp3")
       
       if "was an lmpostor" in image_to_text:
           playsound("wegothim.mp3")
           
  
       

image_to_string()