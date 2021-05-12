import os
import json
from random import choice, randint
from flask import Flask
import crud
from model import connect_to_db, db, Member

app = Flask(__name__)

os.system('dropdb yweb')
os.system('createdb yweb')
db.create_all

crud.create_member("Matilda", "Basner", "matilda.basner@gmail.com", "989-555-1212")

if __name__ == '__main__':
    from server import app

    connect_to_db(app)
