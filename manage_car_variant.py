from flask import Flask, render_template, Blueprint, request, redirect, url_for, flash
import mysql.connector
from db import db, cursor

# BluePrint
manage_car_variant = Blueprint('manage_car_variant', __name__)

# ------------------------------------- Display (select query) Car Model ---------------------------------------------------

# Route to display all Car Variants with details from related tables
@manage_car_variant.route('/manage_car_variant')
def carvariant_table():
    query = """
    SELECT cv.VariantID, 
           m.ModelName, 
           c.ColorName, 
           cc.CategoryName, 
           cv.VariantName, 
           cv.Mileage, 
           cv.Price
    FROM CarVariant cv
    INNER JOIN CarModel m ON cv.ModelID = m.ModelID
    INNER JOIN CarColor c ON cv.ColorID = c.ColorID
    INNER JOIN CarCategory cc ON cv.CategoryID = cc.CategoryID ORDER BY cv.VariantID ASC
    """
    cursor.execute(query)
    data = cursor.fetchall()
    return render_template('manage/view/car_variant.html', data=data)

# ---------------------------------- Route to edit Car Variant ----------------------------------------------------------------

# Route to edit a Car Variant
@manage_car_variant.route('/carvariant/edit/<int:variant_id>', methods=['GET', 'POST'])
def edit_carvariant(variant_id):
    if request.method == 'POST':
        # Retrieve the data from the form
        new_variant_name = request.form['new_variant_name']
        new_model_id = request.form['new_model_id']
        new_color_id = request.form['new_color_id']
        new_category_id = request.form['new_category_id']
        new_mileage = request.form['new_mileage']
        new_price = request.form['new_price']

        try:
            # Update the Car Variant in the database
            update_query = """
                UPDATE CarVariant
                SET VariantName = %s, ModelID = %s, ColorID = %s, CategoryID = %s,
                    Mileage = %s,  Price = %s
                WHERE VariantID = %s
            """
            cursor.execute(update_query, (new_variant_name, new_model_id, new_color_id, new_category_id, new_mileage, new_price, variant_id))
            db.commit()
            flash('Car Variant updated successfully', 'success')
            return render_template('success.html')  # Redirect to the Car Variant list after editing
        except mysql.connector.Error as e:
            db.rollback()
            flash(f'Error updating Car Variant: {e}', 'danger')

    # Fetch Car Variant data for editing and related dropdowns
    fetch_query = """
        SELECT
            cv.VariantID,cv.ModelID, cv.ColorID, cv.CategoryID,cv.VariantName,
            cv.Mileage, cv.Price
        FROM CarVariant cv
        WHERE cv.VariantID = %s
    """
    cursor.execute(fetch_query, (variant_id,))
    variant_data = cursor.fetchone()

    if variant_data is None:
        flash('Car Variant not found', 'danger')
        return redirect(url_for('manage_car_variant.carvariant_table'))  # Redirect to manage variants page

    # Fetch related data for dropdowns
    cursor.execute("SELECT ModelID, ModelName FROM CarModel")
    models = cursor.fetchall()
    cursor.execute("SELECT ColorID, ColorName FROM CarColor")
    colors = cursor.fetchall()
    cursor.execute("SELECT CategoryID, CategoryName FROM CarCategory")
    categories = cursor.fetchall()

    return render_template('manage/edit/edit_car_variant.html', variant_data=variant_data, models=models, colors=colors, categories=categories)


# --------------------------------- Route to delete Car Variant ---------------------------------------------
@manage_car_variant.route('/carvariant/delete/<int:variant_id>', methods=['GET', 'POST'])
def delete_carvariant(variant_id):
    if request.method == 'POST':
        try:
            delete_query = "DELETE FROM CarVariant WHERE VariantID = %s"
            cursor.execute(delete_query, (variant_id,))
            db.commit()
            flash(f"Car Variant with VariantID: {variant_id} deleted successfully", 'success')
            return render_template('success.html')

        except mysql.connector.Error as e:
            db.rollback()
            flash(f'Error deleting Car Variant: {e}', 'danger')

    # Fetch car variant data for confirmation
    fetch_query = """
                   SELECT 
                   cv.VariantID,m.ModelName, c.ColorName, cc.CategoryName,
                   cv.VariantName, cv.Mileage, cv.Price
                   FROM CarVariant cv
                   INNER JOIN CarModel m ON cv.ModelID = m.ModelID
                   INNER JOIN CarColor c ON cv.ColorID = c.ColorID
                   INNER JOIN CarCategory cc ON cv.CategoryID = cc.CategoryID
                   WHERE VariantID = %s
                """

    cursor.execute(fetch_query, (variant_id,))
    variant_data = cursor.fetchone()

    if variant_data is None:
        flash("Car Variant not found", 'danger')
        return redirect(url_for('manage_car_variant.carvariant_table'))

    return render_template('manage/delete/delete_car_variant.html', variant_data=variant_data)