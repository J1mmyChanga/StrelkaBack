import sqlalchemy

from .db_session import SqlAlchemyBase

association_table = sqlalchemy.Table(
    "routes_to_places",
    SqlAlchemyBase.metadata,
    sqlalchemy.Column("route", sqlalchemy.Integer, sqlalchemy.ForeignKey("routes.id")),
    sqlalchemy.Column("place", sqlalchemy.Integer, sqlalchemy.ForeignKey("places.id")))