from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'

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

# ------------------------------------- Display (select query) Car ---------------------------------------------------

# Route to display all Cars
@app.route('/car')
def car_table():
    cursor.execute("SELECT * FROM Car")
    data = cursor.fetchall()
    return render_template('view/car.html', data=data)


# ------------------------------------ Add/Insert Car ---------------------------------------------------

# Route to add a new Car
@app.route('/car/add', methods=['GET', 'POST'])
def add_car():
    if request.method == 'POST':
        variant_id = request.form['variant_id']
        category_id = request.form['category_id']
        engine_id = request.form['engine_id']
        color_id = request.form['color_id']
        model_id = request.form['model_id']
        vin = request.form['vin']
        mileage = request.form['mileage']
        year_of_manufacture = request.form['year_of_manufacture']
        brand_company = request.form['brand_company']
        
        try:
            cursor.execute("INSERT INTO Car (VariantID, CategoryID, EngineID, ColorID, ModelID, VIN, Mileage, YearOfManufacture, BrandCompany) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                           (variant_id, category_id, engine_id, color_id, model_id, vin, mileage, year_of_manufacture, brand_company))
            db.commit()
            flash('Car added successfully', 'success')
            return redirect('/car')
        except mysql.connector.IntegrityError as e:
            db.rollback()
            flash(f'Error adding Car: {e}', 'danger')

    # Fetch the list of variants, categories, engines, colors, and models to populate dropdowns in the form
    cursor.execute("SELECT VariantID, VariantName FROM CarVariant")
    variants = cursor.fetchall()
    cursor.execute("SELECT CategoryID, CategoryName FROM CarCategory")
    categories = cursor.fetchall()
    cursor.execute("SELECT EngineID, EngineName FROM CarEngine")
    engines = cursor.fetchall()
    cursor.execute("SELECT ColorID, ColorName FROM CarColor")
    colors = cursor.fetchall()
    cursor.execute("SELECT ModelID, ModelName FROM CarModel")
    models = cursor.fetchall()

    return render_template('add/add_car.html', variants=variants, categories=categories, engines=engines, colors=colors, models=models)


# ------------------------------------ Update/Edit Car ---------------------------------------------------

# Route to edit a Car
@app.route('/car/edit', methods=['GET', 'POST'])
def edit_car():
    if request.method == 'POST':
        car_id = request.form['car_to_edit']
        new_variant_id = request.form['new_variant_id']
        new_category_id = request.form['new_category_id']
        new_engine_id = request.form['new_engine_id']
        new_color_id = request.form['new_color_id']
        new_model_id = request.form['new_model_id']
        new_vin = request.form['new_vin']
        new_mileage = request.form['new_mileage']
        new_year_of_manufacture = request.form['new_year_of_manufacture']
        new_brand_company = request.form['new_brand_company']
        
        try:
            update_query = "UPDATE Car SET VariantID = %s, CategoryID = %s, EngineID = %s, ColorID = %s, ModelID = %s, VIN = %s, Mileage = %s, YearOfManufacture = %s, BrandCompany = %s WHERE CarID = %s"
            cursor.execute(update_query, (new_variant_id, new_category_id, new_engine_id, new_color_id, new_model_id, new_vin, new_mileage, new_year_of_manufacture, new_brand_company, car_id))
            db.commit()
            flash('Car updated successfully', 'success')
            return redirect('/car')  # Redirect to the Car list after editing
        except mysql.connector.Error as e:
            db.rollback()
            flash(f'Error updating Car: {e}', 'danger')

    # Fetch the list of variants, categories, engines, colors, and models to populate dropdowns in the form
    cursor.execute("SELECT CarID, VariantID, CategoryID, EngineID, ColorID, ModelID, VIN, Mileage, YearOfManufacture, BrandCompany FROM Car")
    cars = cursor.fetchall()
    cursor.execute("SELECT VariantID, VariantName FROM CarVariant")
    variants = cursor.fetchall()
    cursor.execute("SELECT CategoryID, CategoryName FROM CarCategory")
    categories = cursor.fetchall()
    cursor.execute("SELECT EngineID, EngineName FROM CarEngine")
    engines = cursor.fetchall()
    cursor.execute("SELECT ColorID, ColorName FROM CarColor")
    colors = cursor.fetchall()
    cursor.execute("SELECT ModelID, ModelName FROM CarModel")
    models = cursor.fetchall()

    return render_template('update/edit_car.html', cars=cars, variants=variants, categories=categories, engines=engines, colors=colors, models=models)


# --------------------------- Delete Car ---------------------------------------------------

# Route to display the Car deletion form
@app.route('/car/delete', methods=['GET'])
def delete_car_form():
    cursor.execute("SELECT CarID, VIN FROM Car")
    cars = cursor.fetchall()
    return render_template('delete/delete_car.html', cars=cars)

# Route for deleting a Car
@app.route('/car/delete', methods=['POST'])
def delete_car():
    if request.method == 'POST':
        car_id = request.form.get('car_to_delete')

        try:
            cursor.execute("DELETE FROM Car WHERE CarID = %s", (car_id,))
            db.commit()
            flash('Car deleted successfully', 'success')
        except mysql.connector.Error as e:
            db.rollback()
            flash(f'Error deleting Car: {e}', 'danger')

        return redirect('/car')



if __name__ == '__main__':
    app.run(debug=True)
