from flask import Blueprint, render_template

dashboard = Blueprint('dashboard', __name__)

# dashboard for car
@dashboard.route('/car_dashboard')
def car_dashboard():
    return render_template('car.html')

# dashboard for carmodel
@dashboard.route('/carmodel_dashboard')
def carmodel_dashboard():
    return render_template('car_model.html')

# dashboard for carcolor
@dashboard.route('/carcolor_dashboard')
def carcolor_dashboard():
    return render_template('car_color.html')

# dashboard for car category
@dashboard.route('/carcategory_dashboard')
def carcategory_dashboard():
    return render_template('car_category.html')

# dashboard for car engine
@dashboard.route('/carengine_dashboard')
def carengine_dashboard():
    return render_template('car_engine.html')

# dashboard for car variant
@dashboard.route('/carvariant_dashboard')
def carvariant_dashboard():
    return render_template('car_variant.html')
