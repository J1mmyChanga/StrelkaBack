import os

from flask_restful import Api
from flask import Flask, request, flash, redirect, send_from_directory
from werkzeug.serving import WSGIRequestHandler
from werkzeug.utils import secure_filename

from data import db_session

from resources import *

UPLOAD_FOLDER = 'assets'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config["SECRET_KEY"] = "Bebrochka666"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['JSON_AS_ASCII'] = False

db_session.global_init('db/strelka.db')

api = Api(app)
api.add_resource(RegisterResource, "/api/register")
api.add_resource(LoginResource, "/api/login")
api.add_resource(RoutesResource, "/api/routes")
api.add_resource(PlacesResource, "/api/places")


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


@app.route('<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)


def main():
    session = db_session.create_session()
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run(port=8080, host='0.0.0.0')


if __name__ == '__main__':
    main()
