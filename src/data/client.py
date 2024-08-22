import sqlalchemy
from .db_session import SqlAlchemyBase


class Client(SqlAlchemyBase):
    __tablename__ = 'clients'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.CHAR)
    auto_number = sqlalchemy.Column(sqlalchemy.CHAR)
    phone_number = sqlalchemy.Column(sqlalchemy.CHAR)

