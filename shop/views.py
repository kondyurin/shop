import random

from flask import render_template, redirect, session, url_for, request
from sqlalchemy.sql.expression import func

from shop import app, db
from shop.models import Dish, Category


@app.route("/")
def main():
    categories = Category.query.all()
    random_dishes = [random.sample(item.dishes, 3) for item in categories]
    return render_template("main.html", categories=categories, random_dishes=random_dishes)


@app.route("/cart/")
def cart():
    current_cart = session.get('cart', [])
    dish_count = len(current_cart)
    dish_sum = sum(map(int, current_cart))
    return render_template("cart.html", dish_count=dish_count, dish_sum=dish_sum)


@app.route("/add/<dish_price>/")
def add_to_cart(dish_price):
    #сюда надо передавать id блюда а не цену, пока костыль
    cart = session.get('cart', [])
    cart.append(dish_price)
    session['cart'] = cart
    return redirect(url_for(".cart"))