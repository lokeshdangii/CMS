from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint,session
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
from db import db, cursor

# Blueprint
auth = Blueprint('auth',__name__)


# ------------------------------------------------Registration Code -----------------------------------------

@auth.route('/register')
def register_form():
    return render_template('auth/registration.html')

@auth.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Check if the password and confirmation match
        if password != confirm_password:
            flash('Password and confirmation do not match', 'danger')
            return redirect(url_for('auth.register_form'))

        # Hash the password before storing it in the database
        hashed_password = generate_password_hash(password, method='sha256')

        # Insert the user into the database
        insert_user_query = "INSERT INTO User (username, password) VALUES (%s, %s)"
        user_data = (username, hashed_password)

        try:
            cursor.execute(insert_user_query, user_data)
            db.commit()
            flash('Registration successful! You can now login.', 'success')
            return redirect(url_for('auth.login_form'))
        except mysql.connector.Error as e:
            db.rollback()
            flash(f'Registration failed: {e}', 'danger')
            

# ------------------------------------------------Login Code -----------------------------------------
        
@auth.route('/login')
def login_form():
    return render_template('auth/login.html')

@auth.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Query the database to fetch the user's hashed password
        get_user_query = "SELECT username, password FROM User WHERE username = %s"
        cursor.execute(get_user_query, (username,))
        user_data = cursor.fetchone()

        if user_data and check_password_hash(user_data[1], password):
            # Successful login, store user data in session
            session['username'] = user_data[0]
            flash('Login successful!', 'success')
            return redirect(url_for('auth.dashboard'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('auth/login.html')


# ------------------------------------------------ Dashboard -----------------------------------------

@auth.route('/dashboard')
def dashboard():
    # Check if the user is logged in
    if 'username' in session:
        return render_template('car_dashboard.html')
        # return f'Hello, {session["username"]}! Welcome to the dashboard.'
    else:
        return redirect(url_for('auth.login_form'))
    
    
@auth.route('/mydash')
def mydash():
    return render_template('dashboard.html')