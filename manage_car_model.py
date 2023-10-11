from flask import Flask, render_template, Blueprint, request, redirect, url_for, flash
import mysql.connector
from db import db, cursor

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
    return render_template('manage/view/car_model.html', models = models)


# ------------------------------------ Update/Edit Car Model ---------------------------------------------------

# Route to edit a Car Model
@manage_car_model.route('/carmodel/edit/<int:model_id>', methods=['GET', 'POST'])
def edit_carmodel(model_id):
    if request.method == 'POST':

        new_model_name = request.form['new_model_name']
        new_category_id = request.form['new_category_id']
        new_engine_id = request.form['new_engine_id']
        
        try:
            update_query = "UPDATE CarModel SET ModelName = %s, CategoryID = %s, EngineID = %s WHERE ModelID = %s"
            cursor.execute(update_query, (new_model_name, new_category_id, new_engine_id, model_id))
            db.commit()
            flash('Car Model updated successfully', 'success')
            return render_template('success.html')  # Redirect to the Car Model list after editing
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


    return render_template('manage/edit/edit_car_model.html', model_data = model_data, categories=categories, engines=engines)  
    

# --------------------------------- Route to delete Car Model -------------------------------------------------------------------
@manage_car_model.route('/carmodel/delete/<int:model_id>', methods = ['GET','POST'])
def delete_carmodel(model_id):
    if request.method == 'POST':
        try:
            delete_query = "DELETE from CarModel where ModelID = %s"
            cursor.execute(delete_query,(model_id,))
            db.commit()
            flash(f"Car Model with ModelID: { model_id } deleted successfully", 'success')
            return render_template('success.html')

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
    
    return render_template('manage/delete/delete_car_model.html', model_data = model_data)