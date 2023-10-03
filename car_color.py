from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
import mysql.connector
from db import db, cursor


# BluePrint
carcolor = Blueprint('carcolor',__name__)


# ------------------------------------- Display(select query) Car Color ---------------------------------------------------

# Route to display all Car Colors
@carcolor.route('/carcolor')
def carcolor_table():
    cursor.execute("SELECT * FROM CarColor")
    data = cursor.fetchall()
    return render_template('view/carColor.html', data=data)


# ------------------------------------ Add/Insert Car Color ---------------------------------------------------

# Route to add a new Car Color
@carcolor.route('/carcolor/add', methods=['GET', 'POST'])
def add_carcolor():
    if request.method == 'POST':
        color_name = request.form['color_name']
        cursor.execute("INSERT INTO CarColor (ColorName) VALUES (%s)", (color_name,))
        db.commit()
        flash('Car Color added successfully', 'success')
        return redirect(url_for('carcolor_table'))
    return render_template('add/add_carcolor.html')


# ------------------------------------ Update/Edit Car Color ---------------------------------------------------
# Route to edit a Car Color
@carcolor.route('/carcolor/edit', methods=['GET', 'POST'])
def edit_car_color():
    if request.method == 'POST':
        color_id = request.form['color_to_edit']
        new_color_name = request.form['new_color_name']
        
    
        update_query = "UPDATE CarColor SET ColorName = %s WHERE ColorID = %s"
        cursor.execute(update_query, (new_color_name,color_id))
        db.commit()
        
        return redirect('/carcolor')  # Redirect to the Car Color list after editing
    else:
        cursor.execute("SELECT * FROM CarColor")
        colors = cursor.fetchall()
        return render_template('update/edit_carcolor.html', colors=colors)


# --------------------------- delete Car Color ---------------------------------------------------
 
# Route to display the Car Color deletion form
@carcolor.route('/carcolor/delete', methods=['GET'])
def delete_car_color_form():
    cursor.execute("SELECT ColorID, ColorName FROM CarColor")
    colors = cursor.fetchall()
    return render_template('delete/delete_carcolor.html', colors=colors)

# Route for deleting a Car Color
@carcolor.route('/carcolor/delete', methods=['POST'])
def delete_car_color():
    if request.method == 'POST':
        color_id = request.form.get('color_to_delete')

        # Perform the deletion
        try:
            cursor.execute("DELETE FROM CarColor WHERE ColorID = %s", (color_id,))
            db.commit()
        except mysql.connector.Error as err:
            db.rollback()
            return f"Error deleting Car Color: {err}"

        # Redirect back to the Car Color form
        return redirect('/carcolor')


