import random

from flask import render_template, redirect, session, url_for, request
from sqlalchemy.sql.expression import func

from shop import app, db
from shop.models import Dish, Category


@app.route("/")
def main():
    categories = Category.query.all()
    random_dishes = [random.sample(item.dishes, 3) for item in categories]
    current_cart = session.get('cart', [])
    cart_dishes = Dish.query.filter(Dish.id.in_(current_cart)).all()
    return render_template("main.html", categories=categories, random_dishes=random_dishes, cart_dishes=cart_dishes)


@app.route("/cart/")
def cart():
    current_cart = session.get('cart', [])
    cart_dishes = Dish.query.filter(Dish.id.in_(current_cart)).all()
    return render_template("cart.html", cart_dishes=cart_dishes)


@app.route("/add/<int:dish_id>/")
def add_to_cart(dish_id):
    cart = session.get('cart', [])
    cart.append(dish_id)
    session['cart'] = cart
    return redirect(url_for(".cart"))