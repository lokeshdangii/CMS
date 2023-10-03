from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
import mysql.connector
from db import db,cursor


customer = Blueprint('customer',__name__)


# ------------------------------------ Display (Select) Customer ---------------------------------------------------

@customer.route('/customer')
def customer_table():

    cursor.execute("SELECT * FROM Customer")
    data = cursor.fetchall()
    return render_template('view/customer.html', data= data)

# ------------------------------------ Add/Insert Customer ---------------------------------------------------

# Route to add a new Customer
@customer.route('/customer/add', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'POST':
        c_name = request.form['c_name']
        gender = request.form['gender']
        date_of_birth = request.form['date_of_birth']
        phone = request.form['phone']
        email = request.form['email']
        address1 = request.form['address1']
        address2 = request.form['address2']
        city = request.form['city']
        state = request.form['state']
        pincode = request.form['pincode']
        
        try:
            cursor.execute("INSERT INTO Customer (C_Name, Gender, DateOfBirth, Phone, Email, Address1, Address2, City, State, PinCode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                           (c_name, gender, date_of_birth, phone, email, address1, address2, city, state, pincode))
            db.commit()
            flash('Customer added successfully', 'success')
            return redirect('/customer/add')
        except mysql.connector.IntegrityError as e:
            db.rollback()
            flash(f'Error adding Customer: {e}', 'danger')

    return render_template('add/add_customer.html')


# ------------------------------------ Update/Edit Customer ---------------------------------------------------

# Route to edit a Customer
@customer.route('/customer/edit', methods=['GET', 'POST'])
def edit_customer():
    if request.method == 'POST':
        customer_id = request.form['customer_id']
        field_to_update = request.form['field_to_update']
        updated_value = request.form['updated_value']

        try:
            # Construct the update query dynamically based on the selected field
            update_query = f"UPDATE Customer SET {field_to_update} = %s WHERE CustomerID = %s"
            cursor.execute(update_query, (updated_value, customer_id))
            db.commit()
            flash(f'Customer {field_to_update} updated successfully', 'success')
            return redirect('/customer/edit')  # Redirect to the Customer list after editing
        except mysql.connector.Error as e:
            db.rollback()
            flash(f'Error updating Customer: {e}', 'danger')

    # Fetch the list of customers to populate the dropdown in the form
    cursor.execute("SELECT CustomerID, C_Name, Gender, DateOfBirth, Phone, Email, Address1, Address2, City, State, PinCode FROM Customer")
    customers = cursor.fetchall()

    return render_template('update/edit_customer.html', customers=customers)



# --------------------------- Delete Customer ---------------------------------------------------

# Route to display the Customer deletion form
@customer.route('/customer/delete', methods=['GET'])
def delete_customer_form():
    cursor.execute("SELECT CustomerID, C_Name FROM Customer")
    customers = cursor.fetchall()
    return render_template('delete/delete_customer.html', customers=customers)

# Route for deleting a Customer
@customer.route('/customer/delete', methods=['POST'])
def delete_customer():
    if request.method == 'POST':
        c_id = request.form.get('c_to_delete')

        try:
            cursor.execute("DELETE FROM Customer WHERE CustomerID = %s", (c_id,))
            db.commit()
            flash('Customer deleted successfully', 'success')
        except mysql.connector.Error as e:
            db.rollback()
            flash(f'Error deleting Customer: {e}', 'danger')

        return redirect('/customer')
