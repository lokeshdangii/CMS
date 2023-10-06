from flask import Flask, render_template, Blueprint, request, redirect, url_for, flash
import mysql.connector
from db import db, cursor


# BluePrint
manage_car = Blueprint('manage_car', __name__)

@manage_car.route('/manage_car')
def manage_car_table():
    cursor.execute("""
        SELECT 
            C.CarID, 
            CV.VariantName, 
            CC.ColorName, 
            CAT.CategoryName, 
            CE.EngineName, 
            CM.ModelName, 
            C.VIN, 
            C.Mileage, 
            C.YearOfManufacture, 
            C.BrandCompany 
        FROM Car AS C
        JOIN CarVariant AS CV ON C.VariantID = CV.VariantID
        JOIN CarColor AS CC ON C.ColorID = CC.ColorID
        JOIN CarCategory AS CAT ON C.CategoryID = CAT.CategoryID
        JOIN CarEngine AS CE ON C.EngineID = CE.EngineID
        JOIN CarModel AS CM ON C.ModelID = CM.ModelID
    """)
    cars = cursor.fetchall()
    return render_template('manage/manage_car.html', cars=cars)



# Route to edit a car record
@manage_car.route('/car/edit/<int:car_id>', methods=['GET', 'POST'])
def edit_car(car_id):
    if request.method == 'POST':
        variant_id = request.form.get('variant_id')
        category_id = request.form.get('category_id')
        engine_id = request.form.get('engine_id')
        color_id = request.form.get('color_id')
        model_id = request.form.get('model_id')
        vin = request.form.get('vin')
        mileage = request.form.get('mileage')
        year_manufacture = request.form.get('year_manufacture')
        brand_company = request.form.get('brand_company')

        try:
            update_query = """
                UPDATE Car
                SET VariantID = %s, CategoryID = %s, EngineID = %s,
                    ColorID = %s, ModelID = %s, VIN = %s,
                    Mileage = %s, YearOfManufacture = %s, BrandCompany = %s
                WHERE CarID = %s
            """
            cursor.execute(update_query, (variant_id, category_id, engine_id, color_id, model_id,
                                         vin, mileage, year_manufacture, brand_company, car_id))
            db.commit()
            flash('Car updated successfully', 'success')
            return redirect(url_for('manage_car.manage_car_table'))  # Redirect to the manage car page
        except mysql.connector.Error as e:
            db.rollback()
            flash(f'Error updating car: {e}', 'danger')

    # Fetch car data for editing
    fetch_query = "SELECT * FROM Car WHERE CarID = %s"
    cursor.execute(fetch_query, (car_id,))
    car_data = cursor.fetchone()

    if car_data is None:
        flash('Car not found', 'danger')
        return redirect(url_for('manage_car.manage_car_table'))  # Redirect to the manage car page

    return render_template('manage/edit_car.html', car_data=car_data)

# Route to delete a car record
@manage_car.route('/manage_car/delete/<int:car_id>', methods=['GET','POST'])
def delete_car(car_id):
    try:
        delete_query = "DELETE FROM Car WHERE CarID = %s"
        cursor.execute(delete_query, (car_id,))
        db.commit()
        flash('Car deleted successfully', 'success')
    except mysql.connector.Error as e:
        db.rollback()
        flash(f'Error deleting car: {e}', 'danger')

    return redirect(url_for('manage_car.manage_car_table'))  # Redirect to the manage car page





# Route to delete a car record
'''
@manage_car.route('/car/delete/<int:car_id>', methods=['GET', 'POST'])
def delete_car(car_id):
    if request.method == 'POST':
        try:
            delete_query = "DELETE FROM Car WHERE CarID = %s"
            cursor.execute(delete_query, (car_id,))
            db.commit()
            flash('Car deleted successfully', 'success')
            return redirect(url_for('manage_car.manage_car_table'))  # Redirect to the manage car page
        except mysql.connector.Error as e:
            db.rollback()
            flash(f'Error deleting car: {e}', 'danger')

    # Fetch car data for confirmation
    fetch_query = "SELECT * FROM Car WHERE CarID = %s"
    cursor.execute(fetch_query, (car_id,))
    car_data = cursor.fetchone()

    if car_data is None:
        flash('Car not found', 'danger')
        return redirect(url_for('manage_car.manage_car_table'))  # Redirect to the manage car page

    return render_template('manage/delete_car.html', car_data=car_data)
'''