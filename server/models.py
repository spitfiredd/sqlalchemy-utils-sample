from server.extensions import db
# from sqlalchemy import select, Table

# from sqlalchemy_utils.view import create_table_from_selectable
# from sqlalchemy.dialects import postgresql


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    email = db.Column(db.Text)
    premium_user = db.Column(db.Boolean, server_default='FALSE')
