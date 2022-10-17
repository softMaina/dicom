import os
import json
from flask import Flask, request, jsonify, render_template, redirect, flash
from werkzeug.utils import secure_filename
from instance.config import config
from api.models import patient_model
from api.utils.convert_png import convert

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
PATIENT = patient_model.Patient()


def create_app(config_name):
    a = Flask(__name__)
    a.config.from_object(config['development'])

    from api.views import upload_view

    a.register_blueprint(upload_view.upload_route)

    return a


app = create_app(os.getenv('FLASK_ENV'))


@app.errorhandler(Exception)
def handle_error(e):
    if request.mimetype != 'application/json':
        return jsonify({
            'status': 406,
            'message': ''
        }), 406


@app.route('/', methods=['GET', 'POST'])
def home():
    patients = None

    patients = PATIENT.fetch_all_patients()

    if request.method == 'POST':
        if 'file' not in request.files:
            flash('no file')
            return redirect(request.url)
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            data = convert(file=file_path)
            patient_id = data.PatientID
            patient_name = data.PatientName
            patient_birth_date = data.PatientBirthDate
            patient_birth_time = " "
            patient_sex = data.PatientSex

            PATIENT.save(patient_id, patient_name, patient_birth_date, patient_birth_time, patient_sex)

    return render_template('index.html', patients=patients)


if __name__ == '__main__':
    app.run(debug=True)
