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

# Route to display all Car Models
@app.route('/carvariant')
def carengine_table():
    cursor.execute("SELECT * FROM CarVariant")
    data = cursor.fetchall()
    return render_template('view/carVariant.html', data=data)


# ------------------------------------ Add/Insert Car Variant ---------------------------------------------------

# Route to add a new Car Variant
@app.route('/carvariant/add', methods=['GET', 'POST'])
def add_carvariant():
    if request.method == 'POST':
        model_id = request.form['model_id']
        color_id = request.form['color_id']
        category_id = request.form['category_id']
        variant_name = request.form['variant_name']
        mileage = request.form['mileage']
        engine_type = request.form['engine_type']
        price = request.form['price']

        cursor.execute("INSERT INTO CarVariant (ModelID, ColorID, CategoryID, VariantName, Mileage, EngineType, Price) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                       (model_id, color_id, category_id, variant_name, mileage, engine_type, price))
        db.commit()
        flash('Car Variant added successfully', 'success')
        return redirect('/carvariant')
    
    # Fetch the list of models, colors, and categories to populate dropdowns in the form
    cursor.execute("SELECT ModelID, ModelName FROM CarModel")
    models = cursor.fetchall()
    cursor.execute("SELECT ColorID, ColorName FROM CarColor")
    colors = cursor.fetchall()
    cursor.execute("SELECT CategoryID, CategoryName FROM CarCategory")
    categories = cursor.fetchall()

    return render_template('add/add_carvariant.html', models=models, colors=colors, categories=categories)


# ------------------------------------ Edit/Update Car Variant ---------------------------------------------------

# Route to edit a Car Variant
@app.route('/carvariant/edit', methods=['GET', 'POST'])
def edit_carvariant():
    if request.method == 'POST':
        variant_id = request.form['variant_id']
        model_id = request.form['model_id']
        color_id = request.form['color_id']
        category_id = request.form['category_id']
        variant_name = request.form['variant_name']
        mileage = request.form['mileage']
        engine_type = request.form['engine_type']
        price = request.form['price']
        
        try:
            update_query = "UPDATE CarVariant SET ModelID = %s, ColorID = %s, CategoryID = %s, VariantName = %s, Mileage = %s, EngineType = %s, Price = %s WHERE VariantID = %s"
            cursor.execute(update_query, (model_id, color_id, category_id, variant_name, mileage, engine_type, price, variant_id))
            db.commit()
            flash('Car Variant updated successfully', 'success')
            return redirect('/carvariant')  # Redirect to the Car Variant list after editing
        except mysql.connector.Error as e:
            db.rollback()
            flash(f'Error updating Car Variant: {e}', 'danger')

    # Fetch the list of models, colors, and categories to populate dropdowns in the form
    cursor.execute("SELECT VariantID, ModelID, ColorID, CategoryID, VariantName, Mileage, EngineType, Price FROM CarVariant")
    variants = cursor.fetchall()
    cursor.execute("SELECT ModelID, ModelName FROM CarModel")
    models = cursor.fetchall()
    cursor.execute("SELECT ColorID, ColorName FROM CarColor")
    colors = cursor.fetchall()
    cursor.execute("SELECT CategoryID, CategoryName FROM CarCategory")
    categories = cursor.fetchall()

    return render_template('update/edit_carvariant.html', variants=variants, models=models, colors=colors, categories=categories)


# --------------------------- Delete Car Variant ---------------------------------------------------


# Route to display the Car Variant deletion form
@app.route('/carvariant/delete', methods=['GET'])
def delete_carvariant_form():
    cursor.execute("SELECT VariantID FROM CarVariant")
    variants = cursor.fetchall()
    return render_template('delete/delete_carvariant.html', variants=variants)

# Route for deleting a Car Variant
@app.route('/carvariant/delete', methods=['POST'])
def delete_carvariant():
    if request.method == 'POST':
        variant_id = request.form.get('variant_to_delete')

        # Perform the deletion
        try:
            cursor.execute("DELETE FROM CarVariant WHERE VariantID = %s", (variant_id,))
            db.commit()
            flash('Car Variant deleted successfully', 'success')
        except mysql.connector.Error as err:
            db.rollback()
            flash(f'Error deleting Car Variant: {err}', 'danger')

        # Redirect back to the Car Variant deletion form
        return redirect('/carvariant')
    

if __name__ == '__main__':
    app.run(debug=True)

