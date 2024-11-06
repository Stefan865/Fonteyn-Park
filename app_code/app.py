from flask import Flask, render_template, request, redirect, flash
from database import Database, Guest,session, Base, set_password, check_password
from form import NamerForm, LoginForm
from create_pass import pass_create
from datetime import datetime
from email_conf import EmailConfirmation
import os
from flask_login import LoginManager,login_required,login_user
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
D = Database()
secret_key =  D.GetSecretKey()
password = pass_create(10)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///guests.db'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

app.config["SECRET_KEY"] = secret_key

@app.route("/")
def index():
    return render_template("index.html")

@login_manager.user_loader
def load_user(guest_id):
    return Guest.query.get(int(guest_id))

@app.route("/dashboard",methods = ["GET","POST"] )
@login_required
def dashboard():
    return render_template("dashboard.html")


@app.route("/reservation", methods = ["GET","POST"])
def reservation():
    form = NamerForm()
    return render_template("reservation.html",
                           form = form)

@app.route("/checkout", methods = ["GET","POST"])
def checkout():
    if request.method == "POST":
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email_address = request.form['email_address']

        arrival_date_str = request.form['arrivalvalue']
        departure_date_str = request.form['departurevalue']
        arrival_date = datetime.strptime(arrival_date_str, '%Y-%m-%d').date()
        departure_date = datetime.strptime(departure_date_str, '%Y-%m-%d').date()
        people_value = request.form['peoplevalue']
        room1_value = request.form['room1value']
        room2_value = request.form['room2value']
        
        values = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email_address,
            "arrival_date": arrival_date,
            "departure_date": departure_date,
            "num_of_people": people_value,
            "room_1": room1_value,
            "room_2": room2_value
        }
        values1 = [
            first_name, last_name, email_address,
            arrival_date, departure_date, people_value,
            room1_value, room2_value
        ]
        guest = Guest(
            first_name=values["first_name"],
            last_name=values["last_name"],
            email=values["email"],
            arrival_date=values["arrival_date"],
            departure_date=values["departure_date"],
            num_of_people=values["num_of_people"],
            room_1=values["room_1"],
            room_2=values["room_2"],
            password=set_password(password)
        )

        session.add(guest)
        session.commit()
        EmailConfirmation(values1[1],values1[2],values1[3],values1[4],values1[5],values1[6],values1[7],password)
        return render_template("checkout.html", values=values)

    return render_template("checkout.html")

@app.route("/login", methods = ["GET","POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email_address.data
        password = form.password.data
        user = Guest.query.filter(Guest.email==email).one_or_none()
        print(user)

        if user and check_password(set_password(password),password):  
            login_user(user)
            return redirect("/dashboard")
        else:
            flash("Invalid email or password. Please try again.", "error")

    return render_template("login.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)