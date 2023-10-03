from flask import Flask, render_template, request, redirect, url_for, flash,Blueprint
import mysql.connector
from db import db,cursor

installment = Blueprint('installment',__name__)


# ------------------------------ Display Installments ------------------------------

# Route to display all Installments
@installment.route('/installment')
def installment_table():
    cursor.execute("SELECT * FROM Installment")
    data = cursor.fetchall()
    return render_template('view/installment.html', data=data)

# ------------------------------ Add Installment ------------------------------

# Route to add a new Installment
@installment.route('/installment/add', methods=['GET', 'POST'])
def add_installment():
    if request.method == 'POST':
        installment_number = request.form['installment_number']
        due_date = request.form['due_date']
        installment_amount = request.form['installment_amount']
        remaining_amount = request.form['remaining_amount']
        total_installment = request.form['total_installment']

        try:
            cursor.execute("INSERT INTO Installment (InstallmentNumber, DueDate, InstallmentAmount, RemainingAmount, TotalInstallment) VALUES (%s, %s, %s, %s, %s)",
                           (installment_number, due_date, installment_amount, remaining_amount, total_installment))
            db.commit()
            flash('Installment added successfully', 'success')
            return redirect('/installment')
        except mysql.connector.Error as e:
            db.rollback()
            flash(f'Error adding Installment: {e}', 'danger')

    return render_template('add/add_installment.html')

# ------------------------------ Edit Installment ------------------------------

# Route to edit an Installment
@installment.route('/installment/edit', methods=['GET', 'POST'])
def edit_installment():
    if request.method == 'POST':
        installment_id = request.form['installment_id']
        installment_number = request.form['new_installment_number']
        due_date = request.form['new_due_date']
        installment_amount = request.form['new_installment_amount']
        remaining_amount = request.form['new_remaining_amount']
        total_installment = request.form['new_total_installment']

        try:
            update_query = "UPDATE Installment SET InstallmentNumber = %s, DueDate = %s, InstallmentAmount = %s, RemainingAmount = %s, TotalInstallment = %s WHERE InstallmentID = %s"
            cursor.execute(update_query, (installment_number, due_date, installment_amount, remaining_amount, total_installment, installment_id))
            db.commit()
            flash('Installment updated successfully', 'success')
            return redirect('/installment')
        except mysql.connector.Error as e:
            db.rollback()
            flash(f'Error updating Installment: {e}', 'danger')

    return render_template('update/edit_installment.html')

# ------------------------------ Delete Installment ------------------------------

# Route to display the Installment deletion form
@installment.route('/installment/delete', methods=['GET'])
def delete_installment_form():
    cursor.execute("SELECT InstallmentID, InstallmentNumber FROM Installment")
    installments = cursor.fetchall()
    return render_template('delete/delete_installment.html', installments=installments)

# Route for deleting an Installment
@installment.route('/installment/delete', methods=['POST'])
def delete_installment():
    if request.method == 'POST':
        installment_id = request.form.get('installment_to_delete')

        try:
            cursor.execute("DELETE FROM Installment WHERE InstallmentID = %s", (installment_id,))
            db.commit()
            flash('Installment deleted successfully', 'success')
        except mysql.connector.Error as e:
            db.rollback()
            flash(f'Error deleting Installment: {e}', 'danger')

        return redirect('/installment')
