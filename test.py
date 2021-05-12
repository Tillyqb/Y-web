from unittest import TestCase, main
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from model import connect_to_db, Member
# import crud
from sqlalchemy import create_engine
import testing.postgresql
import psycopg2
import os
from crud import create_member

db_uri = 'postgresql:///test'
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    db.init_app(app)
    return app


test_app = create_app()
test_app.app_context().push()

os.system('dropdb test')
os.system('createdb test')
db.create_all
connect_to_db(test_app, db_uri)

with testing.postgresql.Postgresql() as postgresql:
    engine = create_engine(postgresql.url())


class TestCreateMember(TestCase):
    actual = create_member('Matilda', 'Basner', '989-555-1212', 'matildaqb@gmail.com')
    asertin(Matilda, actual)


if __name__ == '__main__':
    main()
