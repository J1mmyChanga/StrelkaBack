import base64

from flask_restful import Resource
from data import db_session
from flask import jsonify, request

from data.users import Users


class LoginResource(Resource):
    @staticmethod
    def post():
        password = request.json["password"]
        email = request.json["email"]

        session = db_session.create_session()
        user: Users = session.query(Users).filter(Users.email == email).first()
        if not user:
            return jsonify({"err": "Wrong nickname"})

        if user.check_password(password):
            return jsonify({
                "id": user.id,
                "email": user.email,
                "image": base64.b64encode(open("." + user.image, "rb").read()).decode("utf-8")
            })
        return jsonify({"err": "Wrong password"})