from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
import mysql.connector
from db import db,cursor

# Blueprint
sale = Blueprint('sale',__name__)

# --------------------------- Sale Table ---------------------------------------------------

# Route to display all Sales
@sale.route('/sale')
def sale_table():
    cursor.execute("""
        SELECT 
            Sale.SaleID, 
            Customer.C_Name, 
            Car.VIN, 
            SalesPerson.SP_Name, 
            Payment.PaymentID, 
            Sale.SaleDate, 
            Sale.SalePrice 
        FROM Sale
        JOIN Customer ON Sale.CustomerID = Customer.CustomerID
        JOIN Car ON Sale.CarID = Car.CarID
        JOIN SalesPerson ON Sale.SalespersonID = SalesPerson.SalespersonID
        JOIN Payment ON Sale.PaymentID = Payment.PaymentID
    """)
    data = cursor.fetchall()
    return render_template('view/sale.html', data=data)


# --------------------------- ADD/Inset in Sale Table ---------------------------------------------------

# Route to add a new Sale
@sale.route('/sale/add', methods=['GET', 'POST'])
def add_sale():
    if request.method == 'POST':
        customer_id = request.form['customer_id']
        car_id = request.form['car_id']
        salesperson_id = request.form['salesperson_id']
        payment_id = request.form['payment_id']
        sale_date = request.form['sale_date']
        sale_price = request.form['sale_price']
        
        try:
            cursor.execute("INSERT INTO Sale (CustomerID, CarID, SalespersonID, PaymentID, SaleDate, SalePrice) VALUES (%s, %s, %s, %s, %s, %s)",
                            (customer_id, car_id, salesperson_id, payment_id, sale_date, sale_price))
            db.commit()
            flash('Sale added successfully', 'success')
            return redirect('/sale')
        except mysql.connector.IntegrityError as e:
            db.rollback()
            flash(f'Error adding Sale: {e}', 'danger')



    # Fetch the list of customers, cars, salespersons, and payments to populate dropdowns in the form
    cursor.execute("SELECT CustomerID, C_Name FROM Customer")
    customers = cursor.fetchall()
    cursor.execute("SELECT CarID, VIN FROM Car")
    cars = cursor.fetchall()
    cursor.execute("SELECT SalesPersonID, SP_Name FROM SalesPerson")
    salespersons = cursor.fetchall()
    cursor.execute("SELECT PaymentID, PaymentID FROM Payment")
    payments = cursor.fetchall()

    return render_template('add/add_sale.html', customers=customers, cars=cars, salespersons=salespersons, payments=payments)

# --------------------------- Edit/UPDATE in Sale Table ---------------------------------------------------

# Route to edit a Sale
@sale.route('/sale/edit', methods=['GET', 'POST'])
def edit_sale():
    if request.method == 'POST':
        sale_id = request.form['sale_to_edit']
        new_customer_id = request.form['new_customer_id']
        new_car_id = request.form['new_car_id']
        new_salesperson_id = request.form['new_salesperson_id']
        new_payment_id = request.form['new_payment_id']
        new_sale_date = request.form['new_sale_date']
        new_sale_price = request.form['new_sale_price']
        
        try:
            update_query = "UPDATE Sale SET CustomerID = %s, CarID = %s, SalespersonID = %s, PaymentID = %s, SaleDate = %s, SalePrice = %s WHERE SaleID = %s"
            cursor.execute(update_query, (new_customer_id, new_car_id, new_salesperson_id, new_payment_id, new_sale_date, new_sale_price, sale_id))
            db.commit()
            flash('Sale updated successfully', 'success')
            return redirect('/sale')  # Redirect to the Sale list after editing
        except mysql.connector.Error as e:
            db.rollback()
            flash(f'Error updating Sale: {e}', 'danger')

    # Fetch the list of sales, customers, cars, salespersons, and payments to populate dropdowns in the form
    cursor.execute("SELECT SaleID, SaleID FROM Sale")
    sales = cursor.fetchall()
    cursor.execute("SELECT CustomerID, C_Name FROM Customer")
    customers = cursor.fetchall()
    cursor.execute("SELECT CarID, VIN FROM Car")
    cars = cursor.fetchall()
    cursor.execute("SELECT SalesPersonID, SP_Name FROM SalesPerson")
    salespersons = cursor.fetchall()
    cursor.execute("SELECT PaymentID, PaymentID FROM Payment")
    payments = cursor.fetchall()

    return render_template('update/edit_sale.html', sales=sales, customers=customers, cars=cars, salespersons=salespersons, payments=payments)


# --------------------------- DELETE Query ---------------------------------------------------

# Route to display the Sale deletion form
@sale.route('/sale/delete', methods=['GET'])
def delete_sale_form():
    cursor.execute("SELECT SaleID, SaleID FROM Sale")
    sales = cursor.fetchall()
    return render_template('delete/delete_sale.html', sales=sales)

# Route for deleting a Sale
@sale.route('/sale/delete', methods=['POST'])
def delete_sale():
    if request.method == 'POST':
        sale_id = request.form.get('sale_to_delete')

        try:
            cursor.execute("DELETE FROM Sale WHERE SaleID = %s", (sale_id,))
            db.commit()
            flash('Sale deleted successfully', 'success')
        except mysql.connector.Error as e:
            db.rollback()
            flash(f'Error deleting Sale: {e}', 'danger')

        return redirect('/sale')

