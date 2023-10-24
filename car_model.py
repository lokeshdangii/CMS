from flask import render_template, Blueprint, request, redirect, url_for, flash, session
import mysql.connector
from db import db, cursor
from auth import login_required

# BluePrint
manage_car_model = Blueprint('manage_car_model', __name__)

# ------------------------------------- Display (select query) Car Model ---------------------------------------------------

# Route to display all Car Models
@manage_car_model.route('/manage_car_model')
def carmodel_table():
    cursor.execute("""
                   select 
                   CM.ModelID, CM.ModelName, CAT.CategoryName,CE.EngineName,CM.Modelspecifications 
                   from CarModel as CM 
                   inner join CarCategory as CAT ON CM.CategoryID = CAT.CategoryID 
                   inner join CarEngine as CE on CM.EngineID = CE.EngineID ORDER BY ModelID ASC
                """)
    
    models = cursor.fetchall()
    return render_template('view/car_model.html', models = models)

# ------------------------------------ Add/Insert Car Model ---------------------------------------------------

# Route to add a new Car Model
@manage_car_model.route('/manage_car_model/add', methods=['GET', 'POST'])
@login_required
def add_carmodel():
    if request.method == 'POST':
        model_name = request.form['model_name']
        category_id = request.form['category_id']
        engine_id = request.form['engine_id']
        model_specifications = request.form['model_specifications']
        
        try:
            cursor.execute("INSERT INTO CarModel (ModelName, CategoryID, EngineID, ModelSpecifications) VALUES (%s, %s, %s, %s)", (model_name, category_id, engine_id,model_specifications))
            db.commit()
            flash('Car Model added successfully', 'success')
            return render_template('success.html')
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
@manage_car_model.route('/carmodel/edit/<int:model_id>', methods=['GET', 'POST'])
@login_required
def edit_carmodel(model_id):
    if request.method == 'POST':

        new_model_name = request.form['new_model_name']
        new_category_id = request.form['new_category_id']
        new_engine_id = request.form['new_engine_id']
        new_model_specification = request.form['new_model_specification']
        
        try:
            update_query = "UPDATE CarModel SET ModelName = %s, CategoryID = %s, EngineID = %s, ModelSpecifications = %s WHERE ModelID = %s"
            cursor.execute(update_query, (new_model_name, new_category_id, new_engine_id, new_model_specification, model_id))
            db.commit()
            flash(f'Car Model with ModelID:{model_id} updated successfully', 'success')
            return redirect(url_for('manage_car_model.carmodel_table'))  # Redirect to the Car Model list after editing
        except mysql.connector.Error as e:
            db.rollback()
            flash(f'Error updating Car Model: {e}', 'danger')

    # Fetch car models for editing and dropdowns
    fetch_query = """
                select 
                CM.ModelID, CM.ModelName, CAT.CategoryName,CE.EngineName,CM.Modelspecifications 
                from CarModel as CM 
                inner join CarCategory as CAT ON CM.CategoryID = CAT.CategoryID 
                inner join CarEngine as CE on CM.EngineID = CE.EngineID
                WHERE CM.ModelID = %s
                """

    cursor.execute(fetch_query, (model_id,))
    model_data = cursor.fetchone()

    if model_data is None:
        flash('Car Model not found','danger')
        return redirect(url_for('manage_car_model.carmodel_table'))  # Redirect to manage models page


    cursor.execute("SELECT CategoryID, CategoryName FROM CarCategory")
    categories = cursor.fetchall()

    cursor.execute("SELECT EngineID, EngineName FROM CarEngine")
    engines = cursor.fetchall()


    return render_template('update/edit_car_model.html', model_data = model_data, categories=categories, engines=engines)  
    

# --------------------------------- Route to delete Car Model -------------------------------------------------------------------
@manage_car_model.route('/carmodel/delete/<int:model_id>', methods = ['GET','POST'])
@login_required
def delete_carmodel(model_id):
    if request.method == 'POST':
        try:
            delete_query = "DELETE from CarModel where ModelID = %s"
            cursor.execute(delete_query,(model_id,))
            db.commit()
            flash(f"Car Model with ModelID: { model_id } deleted successfully", 'success')
            # return render_template('success.html')
            return redirect(url_for('manage_car_model.carmodel_table'))

        except mysql.connector.Error as e:
            db.rollback()
            flash(f'Error deleting Car Model: {e}', 'danger')

         
    # fetch car model data for confirmation
    fetch_query = """
                   select 
                   CM.ModelID, CM.ModelName, CAT.CategoryName,CE.EngineName,CM.Modelspecifications 
                   from CarModel as CM 
                   inner join CarCategory as CAT ON CM.CategoryID = CAT.CategoryID 
                   inner join CarEngine as CE on CM.EngineID = CE.EngineID where ModelID = %s
                """
    
    cursor.execute(fetch_query, (model_id,))
    model_data = cursor.fetchone()

    if model_data is None:
        flash("Car Model not found", 'danger')
        return redirect(url_for('manage_car_model.carmodel_table'))
    
    return render_template('delete/delete_car_model.html', model_data = model_data)