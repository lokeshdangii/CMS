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


# ------------------------------------- Display (select query) Car Categories ---------------------------------------------------

# Route to display all Car Categories
@app.route('/carcategory')
def carcategory_table():
    cursor.execute("SELECT * FROM CarCategory")
    data = cursor.fetchall()
    return render_template('view/carCategory.html', data=data)


# ------------------------------------ Add/Insert Car Category ---------------------------------------------------

# Route to add a new Car Category
@app.route('/carcategory/add', methods=['GET', 'POST'])
def add_carcategory():
    if request.method == 'POST':
        category_id = request.form['category_id']
        category_name = request.form['category_name']
        cursor.execute("INSERT INTO CarCategory (CategoryID,CategoryName) VALUES (%s,%s)", (category_id,category_name,))
        db.commit()
        flash('Car Category added successfully', 'success')
        return redirect(url_for('carcategory_table'))
    return render_template('add/add_carcategory.html')


# ------------------------------------ Update/Edit Car Category ---------------------------------------------------
# Route to edit a Car Category
@app.route('/carcategory/edit', methods=['GET', 'POST'])
def edit_car_category():
    if request.method == 'POST':
        category_id = request.form['category_to_edit']
        new_category_name = request.form['new_category_name']

        update_query = "UPDATE CarCategory SET CategoryName = %s WHERE CategoryID = %s"
        cursor.execute(update_query, (new_category_name, category_id))
        db.commit()

        return redirect('/carcategory')  # Redirect to the Car Category list after editing
    else:
        cursor.execute("SELECT * FROM CarCategory")
        categories = cursor.fetchall()
        return render_template('update/edit_carcategory.html', categories=categories)


# --------------------------- delete Car Category ---------------------------------------------------

# Route to display the Car Category deletion form
@app.route('/carcategory/delete', methods=['GET'])
def delete_car_category_form():
    cursor.execute("SELECT CategoryID, CategoryName FROM CarCategory")
    categories = cursor.fetchall()
    return render_template('delete/delete_carcategory.html', categories=categories)

# Route for deleting a Car Category
@app.route('/carcategory/delete', methods=['POST'])
def delete_car_category():
    if request.method == 'POST':
        category_id = request.form.get('category_to_delete')

        # Perform the deletion
        try:
            cursor.execute("DELETE FROM CarCategory WHERE CategoryID = %s", (category_id,))
            db.commit()
        except mysql.connector.Error as err:
            db.rollback()
            return f"Error deleting Car Category: {err}"

        # Redirect back to the Car Category form
        return redirect('/carcategory')


if __name__ == '__main__':
    app.run(debug=True)
