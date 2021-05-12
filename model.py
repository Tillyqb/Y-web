from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, ForeignKey, String, Column, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class Member(db.Model):
    __tablename__ = 'members'

    id_num = db.Column(db.Integer, primary_key=True, autoincrement=True)
    f_name = db.Column(db.String)
    l_name = db.Column(db.String)
    ph_num = db.Column(db.String)
    email = db.Column(db.String, unique=True)

    def __repr__(self):
        return f'<Member: id num = {self.id_num}, >'


def connect_to_db(flask_app, db_uri='postgresql:///y_web', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')
    return 'success'


if __name__ == '__main__':
    from server import app

    connect_to_db(app)
