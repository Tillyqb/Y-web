from unittest import TestCase, main
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from model import db, connect_to_db
#import crud
from sqlalchemy import create_engine
import testing.postgresql
import psycopg2

with testing.postgresql.Postgresql() as postgresql:
  engine = create_engine(postgresql.url())

class TestConnectToDatabase(TestCase):
  connect_to_db()

if __name__ = '__main__':
  main()