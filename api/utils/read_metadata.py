import os
import pydicom
import csv

# paths to data and save location
filepath = os.getcwd() + '/assets/stage_1_test_images/'  # directory containing the dicom series
dcm_prefix = 'case2_'  # Individual dicom file prefix before number
first_dcm = dcm_prefix + '%04d.dcm' % 1  # first dicom image to inspect metadata fields
new_dir = os.getcwd() + '/data-edited/'  # directory to save new metadata fields


def read_metadata():
    j = 0
    for file in os.listdir(filepath):
        if file.endswith(".dcm"):
            j = j + 1
    total_dcm = 1

    ds = pydicom.filereader.dcmread(filepath + first_dcm)

    for i in range(total_dcm):
        file_number = i + 1
        name = '%04d.dcm' % file_number
        ds = pydicom.filereader.dcmread(filepath + dcm_prefix + name)
        if i == 0:
            ds.SliceLocation = '0.000000'
        else:
            pass
        ds.add_new('0x00200037', 'DS', ['1.000000', '0.000000', '0.000000', '0.000000', '1.000000', '0.000000'])
        ds.save_as(new_dir + dcm_prefix + name)
