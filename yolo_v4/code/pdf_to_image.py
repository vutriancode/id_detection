"""
@author: Vũ Trí An
@version: 1.0
@since March 24 2021
"""
import pdf2image
import os 
import sys

from config import *


link_files  = os.path.abspath(__file__)
print(os.path.join(DATA_PATH,'cmnd1.pdf'))
images = pdf2image.convert_from_path(os.path.join(DATA_PATH,'cmnd1.pdf'))

for image in images:
    COUNT_IMAGE = COUNT_IMAGE +1
    image.save(DATA_PATH+"/data{}.jpg","JPEG")

