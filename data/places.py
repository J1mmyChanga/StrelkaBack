import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Places(SqlAlchemyBase):
    __tablename__ = 'Places'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    long = sqlalchemy.Column(sqlalchemy.Float)
    lat = sqlalchemy.Column(sqlalchemy.Float)
    route_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("routes.id"))

    route = orm.relationship("Routes",
                             secondary="routes_to_places",
                             backref="places")