from flask import render_template, request, redirect, url_for, flash, Blueprint, session
import mysql.connector
from db import db, cursor
from auth import login_required

# BluePrint
manage_car_color = Blueprint('manage_car_color',__name__)


# ------------------------------------- Display(select query) Car Color ---------------------------------------------------

# Route to display all Car Colors
@manage_car_color.route('/manage_car_color')
def carcolor_table():
    cursor.execute("SELECT * FROM CarColor")
    colors = cursor.fetchall()
    return render_template('view/carColor.html', colors = colors)


# ------------------------------------ Add/Insert Car Color ---------------------------------------------------

# Route to add a new Car Color
@manage_car_color.route('/manage_car_color/add', methods=['GET', 'POST'])
@login_required
def add_carcolor():
    if request.method == 'POST':
        color_name = request.form['color_name']
        cursor.execute("INSERT INTO CarColor (ColorName) VALUES (%s)", (color_name,))
        db.commit()
        flash('Car Color added successfully', 'success')
        return redirect(url_for('manage_car_color.carcolor_table'))
    return render_template('add/add_carcolor.html')



# ------------------------------------ Update/Edit Car Color ---------------------------------------------------
# Route to edit a Car Color
@manage_car_color.route('/manage_car_color/edit/<int:color_id>', methods=['GET', 'POST'])
@login_required
def edit_car_color(color_id):
    if request.method == 'POST':
        
        new_color_name = request.form['new_color_name']
        
        try:
            update_query = "UPDATE CarColor SET ColorName = %s WHERE ColorID = %s"
            cursor.execute(update_query, (new_color_name,color_id))
            db.commit()
            flash('Color updated successfully', 'success')
            # return render_template('success.html')
            return redirect(url_for('manage_car_color.carcolor_table'))

        except mysql.connector.Error as e:
            db.rollback()
            flash(f'Error updating Color : {e}', 'danger')
        
    # fetch car color to edit
    fetch_query = "Select ColorID,ColorName from CarColor where ColorID = %s"
    cursor.execute(fetch_query,(color_id,))
    color_data = cursor.fetchone()

    if color_data is None:
        flash('Car Color not found','danger')
        return redirect(url_for('manage_car_color.carcolor_table'))
    
    return render_template('update/edit_carcolor.html', color_data = color_data)



# --------------------------- delete Car Color ---------------------------------------------------

# Route for deleting a Car Color
@manage_car_color.route('/manage_car_color/delete/<int:color_id>', methods=['GET', 'POST'])
@login_required
def delete_car_color(color_id):
    if request.method == 'POST':
        if 'confirmation' in request.form:
            confirmation = request.form['confirmation']
            if confirmation.lower() == 'delete':
                try:
                    # query to delete the car color
                    delete_query = "DELETE FROM CarColor WHERE ColorID = %s"
                    cursor.execute(delete_query, (color_id,))
                    db.commit()

                    flash(f"Car Color with ColorID: {color_id} deleted successfully", 'success')
                    return redirect(url_for('manage_car_color.carcolor_table'))
                except mysql.connector.Error as e:
                    db.rollback()
                    flash(f'Error deleting Car Color: {e}', 'danger')
            else:
                flash('Deletion not confirmed. Please type "delete" to confirm.', 'warning')
        else:
            flash('Invalid request. Confirmation required to delete.', 'warning')

    # Fetch car color to delete
    fetch_query = "SELECT ColorID, ColorName FROM CarColor WHERE ColorID = %s"
    cursor.execute(fetch_query, (color_id,))
    color_data = cursor.fetchone()

    if color_data is None:
        flash('Car Color not found', 'danger')
        return redirect(url_for('manage_car_color.carcolor_table'))

    return render_template('delete/delete_carcolor.html', color_data=color_data)


    # return redirect(url_for('manage_car_color.carcolor_table'))
