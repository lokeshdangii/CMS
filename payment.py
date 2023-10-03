from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
import mysql.connector
from db import db,cursor

payment = Blueprint('payment',__name__)


# ---------------------------- Display (select query) Payment -----------------------------------

# Route to display all Payment records
@payment.route('/payment')
def payment_table():
    cursor.execute("SELECT * FROM Payment")
    data = cursor.fetchall()
    return render_template('view/payment.html', data=data)

# --------------------------- Add/Insert Payment -----------------------------------

# Route to add a new Payment
@payment.route('/payment/add', methods=['GET', 'POST'])
def add_payment():
    if request.method == 'POST':
        installment_id = request.form['installment_id']
        payment_amount = request.form['payment_amount']
        payment_date = request.form['payment_date']
        payment_method = request.form['payment_method']
        transaction_id = request.form['transaction_id']
        payment_due = request.form['payment_due']
        down_payment = request.form['down_payment']
        
        try:
            cursor.execute("INSERT INTO Payment (InstallmentID, PaymentAmount, PaymentDate, PaymentMethod, TransactionID, PaymentDue, DownPayment) VALUES (%s, %s, %s, %s, %s, %s, %s)", (installment_id, payment_amount, payment_date, payment_method, transaction_id, payment_due, down_payment))
            db.commit()
            flash('Payment added successfully', 'success')
            return redirect('/payment')
        except mysql.connector.IntegrityError as e:
            db.rollback()
            flash(f'Error adding Payment: {e}', 'danger')

    # Fetch the list of Installments to populate the dropdown in the form
    cursor.execute("SELECT InstallmentID, InstallmentNumber FROM Installment")
    installments = cursor.fetchall()

    return render_template('add/add_payment.html', installments=installments)

# ---------------------------- Edit/Update Payment -----------------------------------

# Route to edit a Payment
@payment.route('/payment/edit', methods=['GET', 'POST'])
def edit_payment():
    if request.method == 'POST':
        payment_id = request.form['payment_to_edit']
        new_installment_id = request.form['new_installment_id']
        new_payment_amount = request.form['new_payment_amount']
        new_payment_date = request.form['new_payment_date']
        new_payment_method = request.form['new_payment_method']
        new_transaction_id = request.form['new_transaction_id']
        new_payment_due = request.form['new_payment_due']
        new_down_payment = request.form['new_down_payment']
        
        try:
            update_query = "UPDATE Payment SET InstallmentID = %s, PaymentAmount = %s, PaymentDate = %s, PaymentMethod = %s, TransactionID = %s, PaymentDue = %s, DownPayment = %s WHERE PaymentID = %s"
            cursor.execute(update_query, (new_installment_id, new_payment_amount, new_payment_date, new_payment_method, new_transaction_id, new_payment_due, new_down_payment, payment_id))
            db.commit()
            flash('Payment updated successfully', 'success')
            return redirect('/payment')  # Redirect to the Payment list after editing
        except mysql.connector.Error as e:
            db.rollback()
            flash(f'Error updating Payment: {e}', 'danger')

    # Fetch the list of Payments and Installments to populate the dropdowns in the form
    cursor.execute("SELECT PaymentID, InstallmentID, PaymentAmount, PaymentDate, PaymentMethod, TransactionID, PaymentDue, DownPayment FROM Payment")
    payments = cursor.fetchall()
    cursor.execute("SELECT InstallmentID, InstallmentNumber FROM Installment")
    installments = cursor.fetchall()

    return render_template('update/edit_payment.html', payments=payments, installments=installments)

# -------------------------- Delete Payment ---------------------------------

# Route to display the Payment deletion form
@payment.route('/payment/delete', methods=['GET'])
def delete_payment_form():
    cursor.execute("SELECT PaymentID FROM Payment")
    payments = cursor.fetchall()
    return render_template('delete/delete_payment.html', payments=payments)

# Route for deleting a Payment
@payment.route('/payment/delete', methods=['POST'])
def delete_payment():
    if request.method == 'POST':
        payment_id = request.form.get('payment_to_delete')

        try:
            cursor.execute("DELETE FROM Payment WHERE PaymentID = %s", (payment_id,))
            db.commit()
            flash('Payment deleted successfully', 'success')
        except mysql.connector.Error as e:
            db.rollback()
            flash(f'Error deleting Payment: {e}', 'danger')

        return redirect('/payment')

