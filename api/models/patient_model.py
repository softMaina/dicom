from api import database

PATIENTS = []


class Patient:
    def __init__(self):
        self.patient = PATIENTS

    def save(self, patient_id, patient_name, patient_birth_date, patient_birth_time, patient_sex):
        query = """insert into patient ( patient_id, patient_name,  patient_birth_date,
                                   patient_birth_time, patient_sex)
        values ('{}','{}','{}','{}','{}')""".format(patient_id, patient_name, patient_birth_date, patient_birth_time,
                                                    patient_sex)
        database.insert_to_db(query)

    def fetch_all_patients(self):
        query = """select * from patient"""
        return database.select_from_db(query)
