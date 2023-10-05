from flask import Blueprint, render_template

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/car_dashboard')
def car_dashboard():
    return render_template('car.html')

@dashboard.route('/carmodel_dashboard')
def carmodel_dashboard():
    return render_template('car_model.html')

@dashboard.route('/carcolor_dashboard')
def carcolor_dashboard():
    return render_template('car_color.html')

@dashboard.route('/carcategory_dashboard')
def carcategory_dashboard():
    return render_template('car_category.html')

# Add more routes for other sections as needed
