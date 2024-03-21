import base64

from flask_restful import Resource
from data import db_session
from flask import jsonify, request

from data.sex import Sex
from data.users import Users


class RegisterResource(Resource):
    @staticmethod
    def post():
        password = request.json["password"]
        email = request.json["email"]
        image = request.json["image"]

        session = db_session.create_session()
        user = Users(
            email=email,
            image=image,
        )
        user.set_password(password)
        session.add(user)
        session.commit()

        return jsonify("success")