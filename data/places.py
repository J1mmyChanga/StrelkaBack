import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Places(SqlAlchemyBase):
    __tablename__ = 'places'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String)
    description = sqlalchemy.Column(sqlalchemy.String)
    long = sqlalchemy.Column(sqlalchemy.Float)
    lat = sqlalchemy.Column(sqlalchemy.Float)
    rating = sqlalchemy.Column(sqlalchemy.Float)
    image = sqlalchemy.Column(sqlalchemy.BLOB)

    route = orm.relationship("Routes",
                             secondary="routes_to_places",
                             backref="places")