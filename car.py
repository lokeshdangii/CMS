from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
import mysql.connector
from db import db,cursor

car = Blueprint('car',__name__)

# ------------------------------------- Display (select query) Car ---------------------------------------------------

# Route to display all Cars with related information
@car.route('/car')
def car_table():
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
    data = cursor.fetchall()
    return render_template('view/car.html', data=data)



# ------------------------------------ Add/Insert Car ---------------------------------------------------

# Route to add a new Car
@car.route('/car/add', methods=['GET', 'POST'])
def add_car():
    if request.method == 'POST':
        variant_id = request.form['variant_id']
        category_id = request.form['category_id']
        engine_id = request.form['engine_id']
        color_id = request.form['color_id']
        model_id = request.form['model_id']
        vin = request.form['vin']
        mileage = request.form['mileage']
        year_of_manufacture = request.form['year_of_manufacture']
        brand_company = request.form['brand_company']
        
        try:
            cursor.execute("INSERT INTO Car (VariantID, CategoryID, EngineID, ColorID, ModelID, VIN, Mileage, YearOfManufacture, BrandCompany) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                           (variant_id, category_id, engine_id, color_id, model_id, vin, mileage, year_of_manufacture, brand_company))
            db.commit()
            flash('Car added successfully', 'success')
            return redirect('/car')
        except mysql.connector.IntegrityError as e:
            db.rollback()
            flash(f'Error adding Car: {e}', 'danger')

    # Fetch the list of variants, categories, engines, colors, and models to populate dropdowns in the form
    cursor.execute("SELECT VariantID, VariantName FROM CarVariant")
    variants = cursor.fetchall()
    cursor.execute("SELECT CategoryID, CategoryName FROM CarCategory")
    categories = cursor.fetchall()
    cursor.execute("SELECT EngineID, EngineName FROM CarEngine")
    engines = cursor.fetchall()
    cursor.execute("SELECT ColorID, ColorName FROM CarColor")
    colors = cursor.fetchall()
    cursor.execute("SELECT ModelID, ModelName FROM CarModel")
    models = cursor.fetchall()

    return render_template('add/add_car.html', variants=variants, categories=categories, engines=engines, colors=colors, models=models)


# ------------------------------------ Update/Edit Car ---------------------------------------------------

# Route to edit a Car
@car.route('/car/edit', methods=['GET', 'POST'])
def edit_car():
    if request.method == 'POST':
        car_id = request.form['car_id']
        field_to_update = request.form['field_to_update']
        updated_value = request.form['updated_value']

        try:
            # update query on the selected field
            update_query = f"UPDATE Car SET {field_to_update} = %s WHERE CarID = %s"
            cursor.execute(update_query, (updated_value, car_id))
            db.commit()
            flash(f'Car {field_to_update} updated successfully', 'success')
            return redirect('/car/edit')  
        except mysql.connector.Error as e:
            db.rollback()
            flash(f'Error updating Car: {e}', 'danger')

    # Fetch the list of cars to populate the dropdown in the form
    cursor.execute("SELECT Car.CarID, CarModel.ModelName from Car INNER JOIN CarModel ON Car.ModelID = CarModel.ModelID")
    cars = cursor.fetchall()

    return render_template('update/edit_car.html', cars=cars)


# --------------------------- Delete Car ---------------------------------------------------

# Route to display the Car deletion form
@car.route('/car/delete', methods=['GET'])
def delete_car_form():
    cursor.execute("SELECT Car.CarID, CarModel.ModelName from Car INNER JOIN CarModel ON Car.ModelID = CarModel.ModelID;")
    cars = cursor.fetchall()
    return render_template('delete/delete_car.html', cars=cars)

# Route for deleting a Car
@car.route('/car/delete', methods=['POST'])
def delete_car():
    if request.method == 'POST':
        car_id = request.form.get('car_to_delete')

        try:
            cursor.execute("DELETE FROM Car WHERE CarID = %s", (car_id,))
            db.commit()
            flash('Car deleted successfully', 'success')
        except mysql.connector.Error as e:
            db.rollback()
            flash(f'Error deleting Car: {e}', 'danger')

        return redirect('/car/delete')

