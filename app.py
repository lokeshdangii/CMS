from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
import mysql.connector
from db import db, cursor

# import blueprint from scripts
from car_color import carcolor
from car_category import car_category
from car_engine import car_engine
from car_model import car_model
from car_variant import car_variant
from car import car
from salesperson import salesperson
from customer import customer
from installment import installment
from payment import payment
from sale import sale
from finance import finance
from auth import auth


app = Flask(__name__)
app.secret_key = '1df90c98804d9e99099c4356a9d4c3989b681e578d413d79f7759c305b18e6b1'

@app.route("/")
def index():
    return render_template('index.html')


# register blueprint
app.register_blueprint(carcolor)
app.register_blueprint(car_category)
app.register_blueprint(car_engine)
app.register_blueprint(car_model)
app.register_blueprint(car_variant)
app.register_blueprint(car)
app.register_blueprint(salesperson)
app.register_blueprint(customer)
app.register_blueprint(installment)
app.register_blueprint(payment)
app.register_blueprint(sale)
app.register_blueprint(finance)
app.register_blueprint(auth)


if __name__ == '__main__':
    app.run(debug=True)
    
     
# carmodel, carvariant, car, salesperson, customer(edit), Payment, sale and finance