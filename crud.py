from model import connect_to_db, db, Member


def create_member(f_name, l_name, ph_num, email):
    member = Member(f_name=f_name, l_name=l_name, ph_num=ph_num, email=email)

    db.session.add(member)
    db.session.commit()

    return jsonify(member)


if __name__ == '__main__':
    from server import app

    connect_to_db(app)
