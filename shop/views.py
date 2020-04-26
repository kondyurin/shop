import random

from flask import render_template, redirect, session, url_for, request
from sqlalchemy.sql.expression import func
from werkzeug.security import generate_password_hash, check_password_hash

from shop import app, db
from shop.models import Dish, Category, User


@app.route("/")
def main():
    is_auth = session.get('user', {})
    categories = Category.query.all()
    random_dishes = [random.sample(item.dishes, 3) for item in categories]
    current_cart = session.get('cart', [])
    cart_dishes = Dish.query.filter(Dish.id.in_(current_cart)).all()
    return render_template("main.html", categories=categories, random_dishes=random_dishes, cart_dishes=cart_dishes, is_auth=is_auth)


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


@app.route("/del/<int:dish_id>/")
def remove_from_cart(dish_id):
    cart = session.get('cart', [])
    cart.remove(dish_id)
    session['cart'] = cart
    return redirect(url_for(".cart"))


@app.route("/register/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        mail = request.form.get("user_mail")
        password_hash = generate_password_hash(request.form.get("user_password"))
        if not mail or not password_hash:
            return redirect(url_for(".register"))
        user = User(mail=mail, password=password_hash)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for(".cart"))
    return render_template("register.html")


@app.route("/auth/", methods=["GET", "POST"])
def auth():
    if session.get('user'):
        return redirect(url_for(".account"))
    if request.method == "POST":
        mail = request.form.get('user_mail')
        password = request.form.get('user_password')
        user = User.query.filter_by(mail=mail).first()
        if user and user.mail == mail: #сравнивать пароли
            session['user'] = {
                "id": user.id,
                "mail": user.mail
            }
            return redirect(url_for(".account"))
    return render_template("auth.html")


@app.route("/logout/")
def logout():
    session.pop('user')
    return redirect(url_for(".auth"))


@app.route("/account/")
def account():
    return render_template("account.html")