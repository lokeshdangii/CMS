from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
import mysql.connector
from db import db,cursor


manage_car_category = Blueprint('manage_car_category',__name__)


# ------------------------------------- Display (select query) Car Categories ---------------------------------------------------

# Route to display all Car Categories
@manage_car_category.route('/manage_car_category')
def carcategory_table():
    cursor.execute("SELECT * FROM CarCategory")
    data = cursor.fetchall()
    return render_template('view/carCategory.html', data=data)


# ------------------------------------ Add/Insert Car Category ---------------------------------------------------

# Route to add a new Car Category
@manage_car_category.route('/manage_car_category/add', methods=['GET', 'POST'])
def add_carcategory():
    if request.method == 'POST':
        category_id = request.form['category_id']
        category_name = request.form['category_name']
        cursor.execute("INSERT INTO CarCategory (CategoryID,CategoryName) VALUES (%s,%s)", (category_id,category_name,))
        db.commit()
        flash('Car Category added successfully', 'success')
        return redirect(url_for('carcategory_table'))
    return render_template('add/add_carcategory.html')


# ------------------------------------ Update/Edit Car Category ---------------------------------------------------
# Route to edit a Car Category
@manage_car_category.route('/manage_car_category/edit/<int:category_id>', methods=['GET', 'POST'])
def edit_car_category(category_id):
    if request.method == 'POST':

        new_category_name = request.form['new_category_name']

        try:
            update_query = "UPDATE CarCategory SET CategoryName = %s WHERE CategoryID = %s"
            cursor.execute(update_query, (new_category_name,category_id))
            db.commit()
            flash('Category updated successfully', 'success')
            return render_template('success.html')
        
        except mysql.connector.Error as e:
            db.rollback()
            flash(f'Error updating Category : {e}', 'danger')
        
    # fetch car color to edit
    fetch_query = "Select CategoryID,CategoryName from CarCategory where CategoryID = %s"
    cursor.execute(fetch_query,(category_id,))
    category_data = cursor.fetchone()

    if category_data is None:
        flash('Car Category not found','danger')
        return redirect(url_for('manage_car_category.carcategory_table'))
    
    return render_template('update/edit_carcategory.html', category_data = category_data)


# --------------------------- delete Car Category ---------------------------------------------------

# Route for deleting a Car Category
@manage_car_category.route('/manage_car_category/delete/<int:category_id>', methods=['GET','POST'])
def delete_car_category(category_id):
    
    try:
        delete_query = "DELETE from CarCategory where CategoryID = %s"
        cursor.execute(delete_query,(category_id,))
        db.commit()
        flash(f"Car Category with CategoryID: { category_id } deleted successfully", 'success')
        return render_template('success.html')

    except mysql.connector.Error as e:
        db.rollback()
        flash(f'Error deleting Car Category: {e}', 'danger')

    return redirect(url_for('manage_car_category.carcategory_table'))


