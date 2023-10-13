from flask import Blueprint, render_template
import mysql.connector
from db import db, cursor

dashboard = Blueprint('dashboard', __name__)

# Fetch count of tables

# Car Count
cursor.execute("SELECT COUNT(*) FROM Car")
result = cursor.fetchall()
car_count = result[0][0]

# Car Model Count
cursor.execute("SELECT COUNT(*) FROM CarModel")
model_count = cursor.fetchone()

# Variant Count
cursor.execute("SELECT COUNT(*) FROM CarVariant")
variant_count = cursor.fetchone()

# Color Count 
cursor.execute("SELECT COUNT(*) FROM CarColor")
color_count = cursor.fetchone()

# Engine Count
cursor.execute("SELECT COUNT(*) FROM CarEngine")
engine_count = cursor.fetchone()

# Category Count
cursor.execute("SELECT COUNT(*) FROM CarCategory")
category_count = cursor.fetchone()
# Mock counts for demonstration purposes


@dashboard.route('/car_dashboard')
def car_dashboard():
    return render_template('dashboard/car.html',
                           car_count=car_count,  # Access the count value at index 0
                           model_count=model_count[0],
                           variant_count=variant_count[0],
                           color_count=color_count[0],
                           engine_count=engine_count[0],
                           category_count=category_count[0])
