import os


class Config(object):
    DEBUG = True


class Development(Config):
    DEBUG = True
    UPLOAD_FOLDER = "assets"
    DB_URL = "dbname='dicom' host='localhost' port='5432' user='postgres' password='password'"


class Testing(Config):
    DEBUG = True
    Testing = True
    DB_URL = "dbname='dicom_test' host='localhost' port='5432' user='postgres' password='password'"


class Staging(Config):
    DEBUG = True


class Production(Config):
    DEBUG = False
    Testing = False
    DB_URL = "dbname='dicom' host='localhost' port='5432' user='postgres' password='password'"


config = {
    'development': Development,
    'testing': Testing,
    'staging': Staging,
    'production': Production,
    'db_url': "dbname='dicom' host='localhost' port='5432' user='postgres' password='password'",
    "test_db_url": "dbname='dicom_test' host='localhost' port='5432' user='postgres' password='password'"
}
