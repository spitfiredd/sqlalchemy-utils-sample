from server.extensions import db
from sqlalchemy import select
from sqlalchemy_utils import create_view


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    email = db.Column(db.Text)
    premium_user = db.Column(db.Boolean, server_default='FALSE')


class PremiumUserView(db.Model):
    __table_args__ = {'schema': 'public'}
    __table__ = create_view(
        name='premium_users',
        selectable=select([User]).where(User.premium_user == True),
        metadata=db.Model.metadata
    )


# premium_members = select([User]).where(User.premium_user == True)
# print(premium_members)
# create_view('premium_users', premium_members, db.metadata)
