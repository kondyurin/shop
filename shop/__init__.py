import csv

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

from shop.config import BaseConfig


app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from shop.views import *
from shop.models import Dish, Category


def add_dishes_to_db():
    with open('../shop/delivery_items.csv') as f:
        dishes = csv.DictReader(f)
        for item in dishes:
            dish = Dish(id=item['id'],
                        title=item['title'],
                        price=item['price'],
                        description=item['description'],
                        picture=item['picture'],
                        category_id=item['category_id'])
            db.session.add(dish)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()


def add_category_to_db():
    with open('../shop/delivery_categories.csv') as f:
        categories = csv.DictReader(f)
        for item in categories:
            category = Category(id=item['id'],
                        title=item['title'])
            db.session.add(category)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()


# add_dishes_to_db()
# add_category_to_db()
