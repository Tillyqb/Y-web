from server import app
from model import connect_to_db


if __name__ == '__main__':
    from server import app
    connect_to_db(app)