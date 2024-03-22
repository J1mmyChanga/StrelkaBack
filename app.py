import requests
import json

from flask_restful import Api
from flask_httpauth import HTTPTokenAuth
from flask import Flask
from werkzeug.serving import WSGIRequestHandler
from flask_login import LoginManager
from data import db_session


from resources import *

app = Flask(__name__)
app.config["SECRET_KEY"] = "Bebrochka666"
auth = HTTPTokenAuth(scheme='Bearer')

db_session.global_init('db/strelka.db')

login_manager = LoginManager()
login_manager.init_app(app)

api = Api(app)
api.add_resource(RegisterResource, "/api/register")
api.add_resource(LoginResource, "/api/login")
api.add_resource(RoutesResource, "/api/routes")
api.add_resource(PlacesResource, "/api/places")

def main():
    session = db_session.create_session()
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run(port=8080, host='0.0.0.0')


if __name__ == '__main__':
    main()