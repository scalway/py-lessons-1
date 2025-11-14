from flask_login import UserMixin
from extensions import db

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

class Inventory(db.Model):
    __bind_key__ = 'inventory'
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(50))
    name = db.Column(db.String(200))
    category = db.Column(db.String(100))
    brand = db.Column(db.String(100))
    model = db.Column(db.String(100))
    quantity = db.Column(db.Integer)
    weight_kg = db.Column(db.Float)
    price_pln = db.Column(db.Float)
    inventory_value_pln = db.Column(db.Float)