# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
import mysql.connector
from db import db,cursor

finance = Blueprint('finance',__name__)

# ------------------------------------ Display Finance Records ---------------------------------------------------

# Route to display all Finance records
@finance.route('/finance')
def finance_table():
    cursor.execute("SELECT * FROM Finance")
    finances = cursor.fetchall()
    return render_template('view/finance.html', finances=finances)

# ------------------------------------ Add Finance Record ---------------------------------------------------

# Route to add a new Finance record
@finance.route('/finance/add', methods=['GET', 'POST'])
def add_finance():
    if request.method == 'POST':
        sale_id = request.form['sale_id']
        payment_id = request.form['payment_id']
        installment_id = request.form['installment_id']
        financing_term = request.form['financing_term']
        interest_rate = request.form['interest_rate']

        try:
            cursor.execute("INSERT INTO Finance (SaleID, PaymentID, InstallmentID, FinancingTerm, InterestRate) "
                           "VALUES (%s, %s, %s, %s, %s)",
                           (sale_id, payment_id, installment_id, financing_term, interest_rate))
            db.commit()
            flash('Finance record added successfully', 'success')
            return redirect('/finance')
        except mysql.connector.IntegrityError as e:
            db.rollback()
            flash(f'Error adding Finance record: {e}', 'danger')

    # Fetch the list of Sales, Payments, and Installments to populate dropdowns in the form
    cursor.execute("SELECT SaleID, SaleID FROM Sale")
    sales = cursor.fetchall()
    cursor.execute("SELECT PaymentID, PaymentID FROM Payment")
    payments = cursor.fetchall()
    cursor.execute("SELECT InstallmentID, InstallmentID FROM Installment")
    installments = cursor.fetchall()

    return render_template('add/add_finance.html', sales=sales, payments=payments, installments=installments)

# ------------------------------------ Edit Finance Record ---------------------------------------------------

# Route to edit a Finance record
@finance.route('/finance/edit', methods=['GET', 'POST'])
def edit_finance():
    if request.method == 'POST':
        finance_id = request.form['finance_to_edit']
        new_sale_id = request.form['new_sale_id']
        new_payment_id = request.form['new_payment_id']
        new_installment_id = request.form['new_installment_id']
        new_financing_term = request.form['new_financing_term']
        new_interest_rate = request.form['new_interest_rate']

        try:
            update_query = "UPDATE Finance SET SaleID = %s, PaymentID = %s, InstallmentID = %s, " \
                           "FinancingTerm = %s, InterestRate = %s WHERE FinanceID = %s"
            cursor.execute(update_query, (new_sale_id, new_payment_id, new_installment_id, new_financing_term,
                                          new_interest_rate, finance_id))
            db.commit()
            flash('Finance record updated successfully', 'success')
            return redirect('/finance')  # Redirect to the Finance list after editing
        except mysql.connector.Error as e:
            db.rollback()
            flash(f'Error updating Finance record: {e}', 'danger')

    # Fetch the list of Finance records to populate the dropdown in the form
    cursor.execute("SELECT FinanceID, FinanceID FROM Finance")
    finances = cursor.fetchall()

    # Fetch the list of Sales, Payments, and Installments to populate dropdowns in the form
    cursor.execute("SELECT SaleID, SaleID FROM Sale")
    sales = cursor.fetchall()
    cursor.execute("SELECT PaymentID, PaymentID FROM Payment")
    payments = cursor.fetchall()
    cursor.execute("SELECT InstallmentID, InstallmentID FROM Installment")
    installments = cursor.fetchall()

    return render_template('update/edit_finance.html', finances=finances, sales=sales, payments=payments,
                           installments=installments)


# ------------------------------------ Delete Finance Record ---------------------------------------------------

# Route to display the Finance record deletion form
@finance.route('/finance/delete', methods=['GET'])
def delete_finance_form():
    cursor.execute("SELECT FinanceID, FinanceID FROM Finance")
    finances = cursor.fetchall()
    return render_template('delete/delete_finance.html', finances=finances)

# Route for deleting a Finance record
@finance.route('/finance/delete', methods=['POST'])
def delete_finance():
    if request.method == 'POST':
        finance_id = request.form.get('finance_to_delete')

        try:
            cursor.execute("DELETE FROM Finance WHERE FinanceID = %s", (finance_id,))
            db.commit()
            flash('Finance record deleted successfully', 'success')
        except mysql.connector.Error as e:
            db.rollback()
            flash(f'Error deleting Finance record: {e}', 'danger')

        return redirect('/finance')
