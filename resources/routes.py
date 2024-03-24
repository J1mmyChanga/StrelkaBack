from flask_restful import Resource
from flask import jsonify

from data import db_session
from data.routes import Routes


class RoutesResource(Resource):
    @staticmethod
    def get():
        res = []
        session = db_session.create_session()
        routes = session.query(Routes)
        for i in routes:
            d = {
            'id': i.id,
            'title': i.title,
            'description': i.description,
            'duration': i.duration,
            'category': i.category,
            'rating': i.rating,
            }
            res.append(d)
        return jsonify(res)