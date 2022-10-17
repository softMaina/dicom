import json
import sys
import os
import psycopg2
import psycopg2.extras
from flask import jsonify

from instance.config import config


def init_db(db_url=None):
    try:
        if os.getenv('FLASK_ENV') == 'testing':
            conn, cursor = query_database()
            queries = drop_table_if_exists() + create_tables()
        else:
            conn, cursor = query_database()
            queries = create_tables()
        i = 0
        while i != len(queries):
            query = queries[i]
            cursor.execute(query)
            conn.commit()
            i += 1
        conn.close()
    except Exception as error:
        print("DB Error: {} \n".format(error))


def create_tables():
    image_table_query = """ create table Image
(
    SOPInstanceUID       varchar(128) not null
        primary key,
    SeriesInstanceUID    varchar(128),
    DeSOPInstanceUID     varchar(128),
    InstanceNumber    varchar(64),
    SOPClassUID      varchar(128),
    PatientOrientation   varchar(64),
    ContentDate          varchar(64),
    ContentTime          varchar(64),
    ImageType            varchar(64),
    AcquisitionNumber    varchar(64),
    AcquisitionDate      varchar(64),
    AcquisitionTime      varchar(64),
    ImagesinAcquisition  varchar(64),
    ImageComments        varchar(64),
    PresentationLUTShape varchar(64),
    SourcePath           varchar(1024),
    AnonymizedPath       varchar(1024),
    ImageThumbnailPath   varchar(1024),
    DcmStoragePath       varchar(1024)
)"""


patient_table_query = """create table Patient
(
    "PatientUID"       varchar(64) not null
        primary key,
    "PatientID"        varchar(64),
    "PatientName"      varchar(64),
    "DePatientID"      varchar(64),
    "DePatientName"    varchar(64),
    "PatientBirthDate" varchar(64),
    "PatientBirthTime" varchar(64),
    "PatientSex"       varchar(64)
)"""

series_table_query = """create table Series
(
    "SeriesInstanceUID"       varchar(128) not null
        primary key,
    "StudyInstanceUID"        varchar(128),
    "DeSeriesUID"             varchar(128),
    "Modality"                varchar(64),
    "SeiresNumber"            varchar(64),
    "SeriesDate"              varchar(64),
    "SeriesTime"              varchar(64),
    "PerformingPhysicianName" varchar(64),
    "ProtocolName"            varchar(64),
    "SeriesDescription"       varchar(64),
    "OperatorsName"           varchar(64),
    "BodyPartExamined"        varchar(64),
    "PatientPosition"         varchar(64),
    "Laterality"              varchar(64)
)"""

study_table_query = """create table Study
(
    "StudyInstanceUID"       varchar(128) not null
        primary key,
    "PatientUID"             varchar(64)  not null,
    "DeStudyUID"             varchar(128),
    "StudyDate"              varchar(64),
    "StudyTime"              varchar(64),
    "AccessionNumber"        varchar(64),
    "StudyID"                varchar(64),
    "ReferringPhysicianName" varchar(64),
    "StudyDescription"       varchar(64),
    "PatientAge"             varchar(64),
    "PatientSize"            varchar(64),
    "PatientWeight"          varchar(64),
    "StudyBuildTime"         varchar(64)
)"""


def drop_table_if_exists():
    pass


def query_database(query=None, db_url=None):
    conn = None

    if db_url is None:
        db_url = config["development"].DB_URL
    try:
        conn = psycopg2.connect(db_url)
        cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        if query:
            cursor.execute(query)
            conn.commit()
    except(Exception, psycopg2.DatabaseError, psycopg2.ProgrammingError) as error:
        print(error)
        return None

    return conn, cursor


def insert_to_db(query):
    try:
        conn = query_database(query)[0]
        conn.close()
    except psycopg2.Error as error:
        print("Insert error: {}".format(error))
        sys.exit(1)


def select_from_db(query):
    fetched_content = None
    conn, cursor = query_database(query)

    if conn:
        fetched_content = cursor.fetchall()
        conn.close()

    return fetched_content


if __name__ == '__main__':
    init_db()
    query_database()
