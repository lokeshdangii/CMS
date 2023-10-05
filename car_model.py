from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
import mysql.connector
from db import db, cursor

app = Flask(__name__)

car_model = Blueprint('car_model',__name__)

# ------------------------------------- Display (select query) Car Engine ---------------------------------------------------

# Route to display all Car Models
@car_model.route('/carmodel')
def carmodel_table():
    cursor.execute("SELECT * FROM CarModel")
    data = cursor.fetchall()
    return render_template('view/carModel.html', data=data)


# ------------------------------------ Add/Insert Car Model ---------------------------------------------------

# Route to add a new Car Model
@car_model.route('/carmodel/add', methods=['GET', 'POST'])
def add_carmodel():
    if request.method == 'POST':
        model_name = request.form['model_name']
        category_id = request.form['category_id']
        engine_id = request.form['engine_id']
        
        try:
            cursor.execute("INSERT INTO CarModel (ModelName, CategoryID, EngineID) VALUES (%s, %s, %s)", (model_name, category_id, engine_id))
            db.commit()
            flash('Car Model added successfully', 'success')
            return redirect('/carmodel')
        except mysql.connector.IntegrityError as e:
            db.rollback()
            flash(f'Error adding Car Model: {e}', 'danger')

    # Fetch the list of categories and engines to populate dropdowns in the form
    cursor.execute("SELECT CategoryID, CategoryName FROM CarCategory")
    categories = cursor.fetchall()
    cursor.execute("SELECT EngineID, EngineName FROM CarEngine")
    engines = cursor.fetchall()

    return render_template('add/add_carmodel.html', categories=categories, engines=engines)


# ------------------------------------ Update/Edit Car Model ---------------------------------------------------

# Route to edit a Car Model
@car_model.route('/carmodel/edit', methods=['GET', 'POST'])
def edit_carmodel():
    if request.method == 'POST':
        model_id = request.form['model_to_edit']
        new_model_name = request.form['new_model_name']
        new_category_id = request.form['new_category_id']
        new_engine_id = request.form['new_engine_id']
        
        try:
            update_query = "UPDATE CarModel SET ModelName = %s, CategoryID = %s, EngineID = %s WHERE ModelID = %s"
            cursor.execute(update_query, (new_model_name, new_category_id, new_engine_id, model_id))
            db.commit()
            flash('Car Model updated successfully', 'success')
            return redirect('/carmodel')  # Redirect to the Car Model list after editing
        except mysql.connector.Error as e:
            db.rollback()
            flash(f'Error updating Car Model: {e}', 'danger')

    # Fetch the list of categories and engines to populate dropdowns in the form
    cursor.execute("SELECT ModelID, ModelName, CategoryID, EngineID FROM CarModel")
    models = cursor.fetchall()
    cursor.execute("SELECT CategoryID, CategoryName FROM CarCategory")
    categories = cursor.fetchall()
    cursor.execute("SELECT EngineID, EngineName FROM CarEngine")
    engines = cursor.fetchall()

    return render_template('update/edit_carmodel.html', models=models, categories=categories, engines=engines)


# --------------------------- Delete Car Model ---------------------------------------------------

# Route to display the Car Model deletion form
@car_model.route('/carmodel/delete', methods=['GET'])
def delete_carmodel_form():
    cursor.execute("SELECT ModelID, ModelName FROM CarModel")
    models = cursor.fetchall()
    return render_template('delete/delete_carmodel.html', models=models)

# Route for deleting a Car Model
@car_model.route('/carmodel/delete', methods=['POST'])
def delete_carmodel():
    if request.method == 'POST':
        model_id = request.form.get('model_to_delete')

        try:
            cursor.execute("DELETE FROM CarModel WHERE ModelID = %s", (model_id,))
            db.commit()
            flash('Car Model deleted successfully', 'success')
        except mysql.connector.Error as e:
            db.rollback()
            flash(f'Error deleting Car Model: {e}', 'danger')

        return redirect('/carmodel')

