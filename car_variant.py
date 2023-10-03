from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
import mysql.connector
from db import db, cursor

car_variant = Blueprint('car_variant',__name__)

# ------------------------------------- Display (select query) Car Variant ---------------------------------------------------

# Route to display all Car Variants with details from related tables
@car_variant.route('/carvariant')
def carvariant_table():
    query = """
    SELECT cv.VariantName, 
           m.ModelName, 
           c.ColorName, 
           cc.CategoryName, 
           cv.VariantName, 
           cv.Mileage, 
           cv.EngineType, 
           cv.Price
    FROM CarVariant cv
    INNER JOIN CarModel m ON cv.ModelID = m.ModelID
    INNER JOIN CarColor c ON cv.ColorID = c.ColorID
    INNER JOIN CarCategory cc ON cv.CategoryID = cc.CategoryID
    """
    cursor.execute(query)
    data = cursor.fetchall()
    return render_template('view/carVariant.html', data=data)



# ------------------------------------ Add/Insert Car Variant ---------------------------------------------------

# Route to add a new Car Variant
@car_variant.route('/carvariant/add', methods=['GET', 'POST'])
def add_carvariant():
    if request.method == 'POST':
        model_id = request.form['model_id']
        color_id = request.form['color_id']
        category_id = request.form['category_id']
        variant_name = request.form['variant_name']
        mileage = request.form['mileage']
        engine_type = request.form['engine_type']
        price = request.form['price']
        
        if price == '':
            price = None
            
        if mileage == '':
            mileage = 24

        cursor.execute("INSERT INTO CarVariant (ModelID, ColorID, CategoryID, VariantName, Mileage, EngineType, Price) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                       (model_id, color_id, category_id, variant_name, mileage, engine_type, price))
        db.commit()
        flash('Car Variant added successfully', 'success')
        return redirect('/carvariant')
    
    # Fetch the list of models, colors, and categories to populate dropdowns in the form
    cursor.execute("SELECT ModelID, ModelName FROM CarModel")
    models = cursor.fetchall()
    cursor.execute("SELECT ColorID, ColorName FROM CarColor")
    colors = cursor.fetchall()
    cursor.execute("SELECT CategoryID, CategoryName FROM CarCategory")
    categories = cursor.fetchall()

    return render_template('add/add_carvariant.html', models=models, colors=colors, categories=categories)


## ------------------------------------ Edit/Update Car Variant ---------------------------------------------------

# Route to edit a Car Variant
@car_variant.route('/carvariant/edit', methods=['GET', 'POST'])
def edit_carvariant():
    if request.method == 'POST':
        variant_id = request.form['variant_id']
        field_to_update = request.form['field_to_update']
        updated_value = request.form['updated_value']

        try:
            # Construct the update query dynamically based on the selected field
            update_query = f"UPDATE CarVariant SET {field_to_update} = %s WHERE VariantID = %s"
            cursor.execute(update_query, (updated_value, variant_id))
            db.commit()
            flash(f'Car Variant {field_to_update} updated successfully', 'success')
            return redirect('/carvariant')  # Redirect to the Car Variant list after editing
        except mysql.connector.Error as e:
            db.rollback()
            flash(f'Error updating Car Variant: {e}', 'danger')

    # Fetch the list of models, colors, and categories to populate dropdowns in the form
    cursor.execute("SELECT VariantID, ModelID, ColorID, CategoryID, VariantName, Mileage, EngineType, Price FROM CarVariant")
    variants = cursor.fetchall()

    return render_template('update/edit_carvariant.html', variants=variants)


# --------------------------- Delete Car Variant ---------------------------------------------------


# Route to display the Car Variant deletion form
@car_variant.route('/carvariant/delete', methods=['GET'])
def delete_carvariant_form():
    cursor.execute("SELECT VariantID,VariantName FROM CarVariant")
    variants = cursor.fetchall()
    return render_template('delete/delete_carvariant.html', variants=variants)

# Route for deleting a Car Variant
@car_variant.route('/carvariant/delete', methods=['POST'])
def delete_carvariant():
    if request.method == 'POST':
        variant_id = request.form.get('variant_to_delete')

        # Perform the deletion
        try:
            cursor.execute("DELETE FROM CarVariant WHERE VariantID = %s", (variant_id,))
            db.commit()
            flash('Car Variant deleted successfully', 'success')
        except mysql.connector.Error as err:
            db.rollback()
            flash(f'Error deleting Car Variant: {err}', 'danger')

        # Redirect back to the Car Variant deletion form
        return redirect('/carvariant')
    
