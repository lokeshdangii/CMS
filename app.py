from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
import mysql.connector
from db import db, cursor

# import blueprint from scripts
from car_color import manage_car_color
from car_category import manage_car_category
from car_engine import manage_car_engine
from car_model import manage_car_model
from car_variant import manage_car_variant
from car import manage_car
from salesperson import salesperson
from customer import customer
from installment import installment
from payment import payment
from sale import sale
from finance import finance
from auth import auth
from dashboard import dashboard

# # manage part
# from manage_car import manage_car
# from manage_car_model import manage_car_model
# from manage_car_variant import manage_car_variant
# from manage_car_color import manage_car_color
# from manage_car_category import manage_car_category
# from manage_car_engine import manage_car_engine


app = Flask(__name__)
app.secret_key = '1df90c98804d9e99099c4356a9d4c3989b681e578d413d79f7759c305b18e6b1'

@app.route("/")
def index():
    return render_template('auth/login.html')


# register blueprint
app.register_blueprint(manage_car_color)
app.register_blueprint(manage_car_category)
app.register_blueprint(manage_car_engine)
app.register_blueprint(manage_car_model)
app.register_blueprint(manage_car_variant)
app.register_blueprint(manage_car)
app.register_blueprint(salesperson)
app.register_blueprint(customer)
app.register_blueprint(installment)
app.register_blueprint(payment)
app.register_blueprint(sale)
app.register_blueprint(finance)
app.register_blueprint(auth)
app.register_blueprint(dashboard)

# # manage_car
# app.register_blueprint(manage_car)
# app.register_blueprint(manage_car_model)
# app.register_blueprint(manage_car_variant)
# app.register_blueprint(manage_car_color)
# app.register_blueprint(manage_car_category)
# app.register_blueprint(manage_car_engine)

if __name__ == '__main__':
    app.run(debug=True)
    
     
# carmodel, carvariant, car, salesperson, customer(edit), Payment, sale and finance