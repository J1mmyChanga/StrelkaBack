import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Routes(SqlAlchemyBase):
    __tablename__ = 'routes'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String)
    duration = sqlalchemy.Column(sqlalchemy.Integer)
    rating = sqlalchemy.Column(sqlalchemy.Float, sqlalchemy.ForeignKey("season.id"))
    image = sqlalchemy.Column(sqlalchemy.String, nullable=True)