from flask import Flask, make_response, abort, jsonify, Blueprint, request
from api import database
from api.utils.convert_png import convert
from api.models import patient_model
from api.utils.read_metadata import read_metadata
import pydicom as dicom
from pydicom.data import get_testdata_file
import matplotlib.pyplot as plt
import os
import cv2
import PIL
import pandas as pd
import csv
import os
import pydicom
import csv

# Make it True if you want in PNG format
PNG = False

upload_route = Blueprint('upload', __name__, url_prefix='/api/v1/')

PATIENT = patient_model.Patient()


@upload_route.route('upload', methods=['GET'])
def upload():
    read_metadata()
    # data = convert()

    return make_response(jsonify({
        'message': 'uploaded image processing',
        'status': '201'
    }), 201)
