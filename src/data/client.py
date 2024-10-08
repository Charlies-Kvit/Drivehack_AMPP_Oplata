import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from werkzeug.security import generate_password_hash, check_password_hash


class Client(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    login = sqlalchemy.Column(sqlalchemy.CHAR)
    auto_number = sqlalchemy.Column(sqlalchemy.CHAR)
    phone_number = sqlalchemy.Column(sqlalchemy.CHAR, unique=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String)
    last_notification = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now())

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

