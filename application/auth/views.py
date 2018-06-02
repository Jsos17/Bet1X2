from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required

from application import app, db
from application.auth.models import Bettor
from application.auth.forms import LoginForm, BettorForm

@app.route("/auth/login", methods= ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    loginform = LoginForm(request.form)

    bettor = Bettor.query.filter_by(username=loginform.username.data, password=loginform.password.data).first()
    if not bettor:
        return render_template("auth/loginform.html", form = loginform, error="No such username or password")

    login_user(bettor)

    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/new/")
def bettors_form():
    return render_template("auth/new_bettor.html", form = BettorForm())

@app.route("/auth/", methods=["POST"])
def bettor_create():
    form = BettorForm(request.form)

    if not form.validate():
        return render_template("auth/new_bettor.html", form = form)

    b = Bettor(form.username.data, form.password.data, form.balance_eur.data, form.balance_cent.data)
    db.session().add(b)
    db.session().commit()
    flash("Account created successfully, please login to your account")

    return redirect(url_for("auth_login"))

@app.route("/auth/show/<id>", methods=["GET"])
@login_required
def bettor_show(id):
    b = Bettor.query.get(id)
    return render_template("auth/show_user.html", bettor = b)

@app.route("/auth/cancel_update/<id>",  methods=["POST"])
@login_required
def bettor_cancel_update(id):
    return render_template("auth/show_user.html", bettor = Bettor.query.get(id))

@app.route("/auth/update/<id>",  methods=["GET", "POST"])
@login_required
def bettor_update(id):
    if request.method == "POST":
        form = BettorForm(request.form)
        if not form.validate():
            return render_template("auth/update_user.html", form = form, id = id)

        b = Bettor.query.get(id)
        b.username = form.username.data
        b.password = form.password.data
        b.balance_eur = form.balance_eur.data
        b.balance_cent = form.balance_cent.data

        db.session().commit()

        flash("Account updated!")
        return redirect(url_for("bettor_show", id = id))
    else:
        form = BettorForm(obj=Bettor.query.get(id))
        return render_template("auth/update_user.html", form = form, id = id)

@app.route("/auth/delete/<id>", methods=["POST"])
@login_required
def bettor_delete(id):
    b = Bettor.query.get(id)
    db.session().delete(b)
    db.session().commit()
    flash("Account deleted successfully")

    return redirect(url_for("index"))