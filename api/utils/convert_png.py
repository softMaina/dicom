import pydicom as dicom
from pydicom.data import get_testdata_file
import matplotlib.pyplot as plt
import os
import cv2
import PIL
import pandas as pd
import csv


def convert(png=False, file=None):
    dicom_image_description = pd.read_csv(os.getcwd() + "/assets/dicom_image_description.csv")
    ds = dicom.dcmread(file)
    return ds
