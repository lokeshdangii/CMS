from flask import Flask, render_template, Blueprint, request, redirect, url_for, flash, session
import mysql.connector
from db import db, cursor
from auth import login_required
from flask_paginate import Pagination

# BluePrint
manage_car = Blueprint('manage_car', __name__)

#--------------------------- Route to fetch car table --------------------------------------------------------

@manage_car.route('/manage_car')
def manage_car_table():
    page = request.args.get('page', type=int, default=1)
    per_page = 10  # Number of cars per page

    offset = (page - 1) * per_page

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
    C.BrandCompany,  
    CV.VariantID,     
    CC.ColorID,       
    CAT.CategoryID,   
    CE.EngineID,
    CM.ModelID
    FROM Car AS C
    JOIN CarVariant AS CV ON C.VariantID = CV.VariantID
    JOIN CarColor AS CC ON C.ColorID = CC.ColorID
    JOIN CarCategory AS CAT ON C.CategoryID = CAT.CategoryID
    JOIN CarEngine AS CE ON C.EngineID = CE.EngineID
    JOIN CarModel AS CM ON C.ModelID = CM.ModelID
    ORDER BY C.CarID ASC
    LIMIT %s OFFSET %s;
    """, (per_page, offset))

    cars = cursor.fetchall()

    # has_next is a boolean variable that is being assigned the result of the comparison len(cars) == per_page.
    has_next = len(cars) == per_page

    pagination = Pagination(page=page, per_page=per_page)

    return render_template('view/car.html', cars=cars, pagination=pagination, has_next=has_next, page=page, per_page = per_page)
    
# ------------------------------------ Add/Insert Car ---------------------------------------------------

# Route to add a new Car
@manage_car.route('/manage_car/add', methods=['GET', 'POST'])
@login_required
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
            return redirect(url_for('manage_car.manage_car_table'))  # Redirect to the manage car page
        
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



# ---------------------------------- Route to edit Car ----------------------------------------------------------------

# Route to edit a car record
@manage_car.route('/car/edit/<int:car_id>', methods=['GET', 'POST'])
@login_required
def edit_car(car_id):
    if request.method == 'POST':
        variant_id = request.form.get('variant_id')
        category_id = request.form.get('category_id')
        engine_id = request.form.get('engine_id')
        color_id = request.form.get('color_id')
        model_id = request.form.get('model_id')
        mileage = request.form.get('mileage')
        year_manufacture = request.form.get('year_manufacture')
        brand_company = request.form.get('brand_company')

        try:
            update_query = """
                UPDATE Car
                SET VariantID = %s, CategoryID = %s, EngineID = %s,
                    ColorID = %s, ModelID = %s, 
                    Mileage = %s, YearOfManufacture = %s, BrandCompany = %s
                WHERE CarID = %s
            """
            cursor.execute(update_query, (variant_id, category_id, engine_id, color_id, model_id,
                                             mileage, year_manufacture, brand_company, car_id))
            db.commit()
            flash('Car updated successfully', 'success')
            # return render_template('success.html')
            return redirect(url_for('manage_car.manage_car_table'))  # Redirect to the manage car page
        
        except mysql.connector.Error as e:
            db.rollback()
            flash(f'Error updating car: {e}', 'danger')

    # Fetch car data for editing and dropdowns
    fetch_query = """
        SELECT
        C.CarID,
        CV.VariantId, 
        CAT.CategoryID, 
        CE.EngineID, 
        CC.ColorId, 
        CM.ModelId,  
        C.Mileage, 
        C.YearOfManufacture, 
        C.BrandCompany 
        FROM Car AS C         
        JOIN CarVariant AS CV ON C.VariantID = CV.VariantID
        JOIN CarColor AS CC ON C.ColorID = CC.ColorID         
        JOIN CarCategory AS CAT ON C.CategoryID = CAT.CategoryID         
        JOIN CarEngine AS CE ON C.EngineID = CE.EngineID         
        JOIN CarModel AS CM ON C.ModelID = CM.ModelID 
        WHERE C.CarID = %s 
        """
    cursor.execute(fetch_query, (car_id,))
    car_data = cursor.fetchone()
  

    if car_data is None:
        flash('Car not found', 'danger')
        return redirect(url_for('manage_car.manage_car_table'))  # Redirect to the manage car page

    # Fetch data for dropdowns
    cursor.execute("SELECT * FROM CarVariant")
    variants = cursor.fetchall()
    # print("variants = ", variants)

    cursor.execute("SELECT * FROM CarCategory")
    categories = cursor.fetchall()

    cursor.execute("SELECT * FROM CarEngine")
    engines = cursor.fetchall()

    cursor.execute("SELECT * FROM CarColor")
    colors = cursor.fetchall()

    cursor.execute("SELECT * FROM CarModel")
    models = cursor.fetchall()

    # Pass the data to the HTML template
    return render_template('update/edit_car.html', car_data=car_data, variants=variants, categories=categories, engines=engines, colors=colors, models=models)



# --------------------------------- Route to delete Car ------------------------------------------------------
@manage_car.route('/car/delete/<int:car_id>', methods=['GET', 'POST'])
@login_required
def delete_car(car_id):
    if request.method == 'POST':
        try:
            delete_query = "DELETE FROM Car WHERE CarID = %s"
            cursor.execute(delete_query, (car_id,))
            db.commit()
            flash(f'Car with CarID: { car_id } deleted successfully', 'success')
            return redirect(url_for('manage_car.manage_car_table'))  # Redirect to the manage car page
            # return render_template('success.html')
            
        except mysql.connector.Error as e:
            db.rollback()
            flash(f'Error deleting car: {e}', 'danger')

    # Fetch car data for confirmation
    fetch_query = """
        SELECT
        C.CarID,
        CV.VariantName, 
        CAT.CategoryName, 
        CE.EngineName, 
        CC.ColorName, 
        CM.ModelName, 
        C.Mileage, 
        C.YearOfManufacture, 
        C.BrandCompany 
        FROM Car AS C         
        JOIN CarVariant AS CV ON C.VariantID = CV.VariantID
        JOIN CarColor AS CC ON C.ColorID = CC.ColorID         
        JOIN CarCategory AS CAT ON C.CategoryID = CAT.CategoryID         
        JOIN CarEngine AS CE ON C.EngineID = CE.EngineID         
        JOIN CarModel AS CM ON C.ModelID = CM.ModelID 
        WHERE C.CarID = %s 
        """
    cursor.execute(fetch_query, (car_id,))
    car_data = cursor.fetchone()

    if car_data is None:
        flash('Car not found', 'danger')
        return redirect(url_for('manage_car.manage_car_table'))  # Redirect to the manage car page

    return render_template('delete/delete_car.html', car_data=car_data)

