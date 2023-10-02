from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "cardb"
}

# Create a connection to the MySQL database
db = mysql.connector.connect(**db_config)

# Initialize a cursor
cursor = db.cursor()

# ------------------------------------- Display (select query) Car Engine ---------------------------------------------------

# Route to display all Car Engines
@app.route('/carengine')
def carengine_table():
    cursor.execute("SELECT * FROM CarEngine")
    data = cursor.fetchall()
    return render_template('view/carEngine.html', data=data)


# ------------------------------------ Add/Insert Car Engine ---------------------------------------------------

# Route to add a new Car Engine
@app.route('/carengine/add', methods=['GET', 'POST'])
def add_carengine():
    if request.method == 'POST':
        engine_id = request.form['engine_id']
        engine_name = request.form['engine_name']
        
        try:
            cursor.execute("INSERT INTO CarEngine (EngineID, EngineName) VALUES (%s, %s)", (engine_id, engine_name))
            db.commit()
            flash('Car Engine added successfully', 'success')
            return render_template('add/add_carengine.html')
        except mysql.connector.IntegrityError as e:
            db.rollback()
            return f'Error adding Car Engine: {e}', 'danger'
    

    return render_template('add/add_carengine.html')



# ------------------------------------ Update/Edit Car Engine ---------------------------------------------------
# Route to edit a Car Engine
@app.route('/carengine/edit', methods=['GET', 'POST'])
def edit_car_engine():
    if request.method == 'POST':
        engine_id = request.form['engine_to_edit']
        new_engine_name = request.form['new_engine_name']

        update_query = "UPDATE CarEngine SET EngineName = %s WHERE EngineID = %s"
        cursor.execute(update_query, (new_engine_name, engine_id))
        db.commit()

        return redirect('/carengine')  # Redirect to the Car Engine list after editing
    else:
        cursor.execute("SELECT * FROM CarEngine")
        engines = cursor.fetchall()
        return render_template('update/edit_carengine.html', engines=engines)


# --------------------------- delete Car Engine ---------------------------------------------------

# Route to display the Car Engine deletion form
@app.route('/carengine/delete', methods=['GET'])
def delete_car_engine_form():
    cursor.execute("SELECT EngineID, EngineName FROM CarEngine")
    engines = cursor.fetchall()
    return render_template('delete/delete_carengine.html', engines=engines)

# Route for deleting a Car Engine
@app.route('/carengine/delete', methods=['POST'])
def delete_car_engine():
    if request.method == 'POST':
        engine_id = request.form.get('engine_to_delete')

        # Perform the deletion
        try:
            cursor.execute("DELETE FROM CarEngine WHERE EngineID = %s", (engine_id,))
            db.commit()
        except mysql.connector.Error as err:
            db.rollback()
            return f"Error deleting Car Engine: {err}"

        # Redirect back to the Car Engine deletion form
        return redirect('/carengine/delete')

if __name__ == '__main__':
    app.run(debug=True)