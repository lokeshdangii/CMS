from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
import mysql.connector
from db import db, cursor

# Blueprint
salesperson = Blueprint('salesperson',__name__)


# ------------------------------------- Display(select query) Salesperson ---------------------------------------------------

# Route to display all Car Colors
@salesperson.route('/salesperson')
def salesperson_table():
    cursor.execute("SELECT * FROM SalesPerson")
    data = cursor.fetchall()
    return render_template('view/salesperson.html', data=data)

# ------------------------------------ Add/Insert SalesPerson ---------------------------------------------------

# Route to add a new SalesPerson
@salesperson.route('/salesperson/add', methods=['GET', 'POST'])
def add_salesperson():
    if request.method == 'POST':
        sp_name = request.form['sp_name']
        gender = request.form['gender']
        date_of_birth = request.form['date_of_birth']
        mobile_no = request.form['mobile_no']
        email = request.form['email']
        address1 = request.form['address1']
        address2 = request.form['address2']
        city = request.form['city']
        state = request.form['state']
        pincode = request.form['pincode']
        
        try:
            cursor.execute("INSERT INTO SalesPerson (SP_Name, Gender, DateOfBirth, MobileNo, email, Address1, Address2, City, State, PinCode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                           (sp_name, gender, date_of_birth, mobile_no, email, address1, address2, city, state, pincode))
            db.commit()
            flash('SalesPerson added successfully', 'success')
            return redirect('/salesperson')
        except mysql.connector.IntegrityError as e:
            db.rollback()
            flash(f'Error adding SalesPerson: {e}', 'danger')

    return render_template('add/add_salesperson.html')


# ------------------------------------ Update/Edit SalesPerson ---------------------------------------------------

# Route to edit a SalesPerson
@salesperson.route('/salesperson/edit', methods=['GET', 'POST'])
def edit_salesperson():
    if request.method == 'POST':
        salesperson_id = request.form['salesperson_id']
        field_to_update = request.form['field_to_update']
        updated_value = request.form['updated_value']

        try:
            # Construct the update query dynamically based on the selected field
            update_query = f"UPDATE SalesPerson SET {field_to_update} = %s WHERE SalesPersonID = %s"
            cursor.execute(update_query, (updated_value, salesperson_id))
            db.commit()
            flash(f'SalesPerson {field_to_update} updated successfully', 'success')
            return redirect('/salesperson/edit')  
        except mysql.connector.Error as e:
            db.rollback()
            flash(f'Error updating SalesPerson: {e}', 'danger')

    # Fetch the list of salespersons to populate the dropdown in the form
    cursor.execute("SELECT SalesPersonID, SP_Name, Gender, DateOfBirth, MobileNo, email, Address1, Address2, City, State, PinCode FROM SalesPerson")
    salespersons = cursor.fetchall()

    return render_template('update/edit_salesperson.html', salespersons=salespersons)



# --------------------------- Delete SalesPerson ---------------------------------------------------

# Route to display the SalesPerson deletion form
@salesperson.route('/salesperson/delete', methods=['GET'])
def delete_salesperson_form():
    cursor.execute("SELECT SalesPersonID, SP_Name FROM SalesPerson")
    salespersons = cursor.fetchall()
    return render_template('delete/delete_salesperson.html', salespersons=salespersons)

# Route for deleting a SalesPerson
@salesperson.route('/salesperson/delete', methods=['POST'])
def delete_salesperson():
    if request.method == 'POST':
        sp_id = request.form.get('sp_to_delete')

        try:
            cursor.execute("DELETE FROM SalesPerson WHERE SalesPersonID = %s", (sp_id,))
            db.commit()
            flash('SalesPerson deleted successfully', 'success')
        except mysql.connector.Error as e:
            db.rollback()
            flash(f'Error deleting SalesPerson: {e}', 'danger')

        return redirect('/salesperson')

