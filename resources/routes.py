from flask_restful import Resource
from flask import jsonify


class RoutesResource(Resource):
    @staticmethod
    def get():
        res = []
        return jsonify(res)