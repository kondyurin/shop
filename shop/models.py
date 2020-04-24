from datetime import datetime

from shop import db


order_dishes = db.Table('order_dishes',
                        db.Column('order_id', db.Integer, db.ForeignKey('orders.id')),
                        db.Column('dish_id', db.Integer, db.ForeignKey('dishes.id'))
                        )


class Dish(db.Model):
    __tablename__ = 'dishes'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    price = db.Column(db.Integer)
    description = db.Column(db.String)
    picture = db.Column(db.String)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    category = db.relationship('Category', back_populates='dishes')
    orders = db.relationship('Order', secondary='order_dishes', back_populates='dishes')


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    dishes = db.relationship('Dish', back_populates='category')


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    mail = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    orders = db.relationship('Order', back_populates='user')


class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    amount = db.Column(db.Integer)
    status = db.Column(db.Boolean, default=False)
    mail = db.Column(db.String)
    phone = db.Column(db.String, unique=True)
    address = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates='orders')
    dishes = db.relationship('Dish', secondary='order_dishes', back_populates='orders')