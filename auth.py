from flask import render_template, request, redirect, url_for, flash, Blueprint,session
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
from db import db, cursor
from functools import wraps

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
        
        # Check if the username already exists
        check_user_query = "SELECT Username FROM User WHERE Username = %s"
        cursor.execute(check_user_query, (username,))
        existing_user = cursor.fetchone()   

        if existing_user:
            flash('Username already exists. Please choose a different username.', 'danger')
            return redirect(url_for('auth.register_form'))

        # Hash the password before storing it in the database
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        # Insert the user into the database
        insert_user_query = "INSERT INTO User (Username, Password, role) VALUES (%s, %s, 'User')"
        user_data = (username, hashed_password)

        try:
            cursor.execute(insert_user_query, user_data)
            db.commit()
            flash('Registration successful! You can now login.', 'success')
            return redirect(url_for('auth.user_login_form'))
        except mysql.connector.Error as e:
            db.rollback()
            flash(f'Registration failed: {e}', 'danger')
            

# ------------------------------------------------Admin Login Code -----------------------------------------
        
@auth.route('/login')
def login_form():
    return render_template('auth/adminlogin.html')

@auth.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Query the database to fetch the user's hashed password
        get_user_query = "SELECT Username, Password, role FROM Admin WHERE Username = %s"
        cursor.execute(get_user_query, (username,))
        user_data = cursor.fetchone()

        if user_data and password:
            # Successful login, store user data in session
            session['username'] = user_data[0] # Store the username in the session
            session['role'] = user_data[2]  # Store the role in the session
            flash('Login successful!', 'success')
            return redirect(url_for('auth.dashboard'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('auth/adminlogin.html')


# -------------------------------------------- User Login Code ----------------------------------------

@auth.route('/userlogin')
def user_login_form():
    return render_template('auth/userlogin.html')

@auth.route('/userlogin', methods=['POST'])
def user_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Query the database to fetch the user's hashed password
        get_user_query = "SELECT Username, Password, role FROM User WHERE Username = %s"
        cursor.execute(get_user_query, (username,))
        user_data = cursor.fetchone()

        if user_data and check_password_hash(user_data[1], password):
            # Successful login, store user data in session
            session['username'] = user_data[0]  # Store the username in the session
            session['role'] = user_data[2]    # Store the role in the session
            flash('Login successful!', 'success')
            return redirect(url_for('auth.dashboard'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('auth/userlogin.html')



# ------------------------------------------------Logout Code -----------------------------------------

@auth.route('/logout')
def logout():
    # Clear the session to log the user out
    session.pop('username', None)
    # flash('You have been logged out.', 'info')
    return render_template('index.html')


# ------------------------------------------- Login Required for Authentification -------------------------

# the login_required function
def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if session.get('username'):
            # User is authenticated, execute the original view function
            return view(*args, **kwargs)
        else:
            # User is not authenticated, redirect to the login page
            flash("You are not logged in..! Login to perform action")
            return redirect(url_for('auth.login_form'))

    return wrapped_view




# ------------------------------------------------ Dashboard -----------------------------------------

# Fetch count of tables

# Car Count
cursor.execute("SELECT COUNT(*) FROM Car")
car_count = cursor.fetchone()

# Car Model Count
cursor.execute("SELECT COUNT(*) FROM CarModel")
model_count = cursor.fetchone()

# Variant Count
cursor.execute("SELECT COUNT(*) FROM CarVariant")
variant_count = cursor.fetchone()

# Color Count 
cursor.execute("SELECT COUNT(*) FROM CarColor")
color_count = cursor.fetchone()

# Engine Count
cursor.execute("SELECT COUNT(*) FROM CarEngine")
engine_count = cursor.fetchone()

# Category Count
cursor.execute("SELECT COUNT(*) FROM CarCategory")
category_count = cursor.fetchone()


# ---------------------------- Route for DASHBOARD ------------------------------------------

@auth.route('/dashboard')
def dashboard():
    # Check if the user is logged in
    if 'username' in session:
        
        return render_template('dashboard.html',
                           car_count=car_count[0],  # Access the count value directly
                           model_count=model_count[0],  # Access the first element of the tuple
                           variant_count=variant_count[0],
                           color_count=color_count[0],
                           engine_count=engine_count[0],
                           category_count=category_count[0])
    else:
        return redirect(url_for('auth.login_form'))
