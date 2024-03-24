import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Routes(SqlAlchemyBase):
    __tablename__ = 'routes'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String)
    description = sqlalchemy.Column(sqlalchemy.String)
    duration = sqlalchemy.Column(sqlalchemy.Integer)
    rating = sqlalchemy.Column(sqlalchemy.Float)
    category = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("categories.id"))

    categories = orm.relationship(
        "Categories",
        backref="routes"
    )