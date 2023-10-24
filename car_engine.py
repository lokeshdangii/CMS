from flask import render_template, request, redirect, url_for, flash, Blueprint, session
from db import db,cursor
import mysql.connector
from auth import login_required

manage_car_engine = Blueprint('manage_car_engine',__name__)

# ------------------------------------- Display (select query) Car Engine ---------------------------------------------------

# Route to display all Car Engines
@manage_car_engine.route('/manage_car_engine')
def carengine_table():
    cursor.execute("SELECT EngineID,EngineName FROM CarEngine")
    data = cursor.fetchall()
    return render_template('view/carEngine.html', data=data, )


# ------------------------------------ Add/Insert Car Engine ---------------------------------------------------

# Route to add a new Car Engine
@manage_car_engine.route('/manage_car_engine/add', methods=['GET', 'POST'])
@login_required
def add_carengine():
    if request.method == 'POST':
        # engine_id = request.form['engine_id']
        engine_name = request.form['engine_name']
        
        try:
            cursor.execute("INSERT INTO CarEngine (EngineName) VALUES (%s)", (engine_name,))
            db.commit()
            flash('Car Engine added successfully', 'success')
            return redirect(url_for('manage_car_engine.carengine_table'))
        except mysql.connector.IntegrityError as e:
            db.rollback()
            return f'Error adding Car Engine: {e}', 'danger'
    

    return render_template('add/add_carengine.html')



# ------------------------------------ Update/Edit Car Engine ---------------------------------------------------
# Route to edit a Car Engine
@manage_car_engine.route('/manage_car_engine/edit/<int:engine_id>', methods=['GET', 'POST'])
@login_required
def edit_car_engine(engine_id):
    if request.method == 'POST':
        
        new_engine_name = request.form['new_engine_name']

        try:
            update_query = "UPDATE CarEngine SET EngineName = %s WHERE EngineID = %s"
            cursor.execute(update_query, (new_engine_name,engine_id))
            db.commit()
            flash('Car Engine updated successfully', 'success')
            # return render_template('success.html')
            return redirect(url_for('manage_car_engine.carengine_table'))
        
        except mysql.connector.Error as e:
            db.rollback()
            flash(f'Error updating Car Engine : {e}', 'danger')
        
    # fetch car color to edit
    fetch_query = "Select EngineID,EngineName from CarEngine where EngineID = %s"
    cursor.execute(fetch_query,(engine_id,))
    engine_data = cursor.fetchone()

    if engine_data is None:
        flash('Car Engine not found','danger')
        return redirect(url_for('manage_car_engine.carengine_table'))
    
    return render_template('update/edit_carengine.html', engine_data = engine_data)



# --------------------------- delete Car Engine ---------------------------------------------------

# Route for deleting a Car Engine
@manage_car_engine.route('/manage_car_engine/delete/<int:engine_id>', methods=['GET', 'POST'])
@login_required
def delete_car_engine(engine_id):
    if request.method == 'POST':
        if 'confirmation' in request.form:
            confirmation = request.form['confirmation']
            if confirmation.lower() == 'delete':
                try:
                    # query to delete the engine
                    delete_query = "DELETE FROM CarEngine WHERE EngineID = %s"
                    cursor.execute(delete_query, (engine_id,))
                    db.commit()

                    flash(f"Car Engine with EngineID: {engine_id} and associated cars deleted successfully", 'success')
                    return redirect(url_for('manage_car_engine.carengine_table'))
                except mysql.connector.Error as e:
                    db.rollback()
                    flash(f'Error deleting Car Engine: {e}', 'danger')
            else:
                flash('Deletion not confirmed. Please type "delete" to confirm.', 'warning')
        else:
            flash('Invalid request. Confirmation required to delete.', 'warning')

    # Fetch car engine to delete
    fetch_query = "SELECT EngineID, EngineName FROM CarEngine WHERE EngineID = %s"
    cursor.execute(fetch_query, (engine_id,))
    engine_data = cursor.fetchone()

    if engine_data is None:
        flash('Car Engine not found', 'danger')
        return redirect(url_for('manage_car_engine.carengine_table'))

    return render_template('delete/delete_carengine.html', engine_data=engine_data)
