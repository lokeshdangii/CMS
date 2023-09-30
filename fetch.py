from flask import Flask, render_template
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

# Routing

# main page route
@app.route("/")
def index():
    return render_template('index.html')

# --> 1 route to fetch and render Car table
@app.route('/car')
def car_table():
    
    cursor.execute("SELECT * FROM Car")
    data = cursor.fetchall()
    return render_template('view/car.html', data=data)


# --> 2 route to fetch and render Car color table
@app.route('/carcolor')
def carcolor_table():
    
    cursor.execute("SELECT * FROM CarColor")
    data = cursor.fetchall()
    return render_template('view/carColor.html', data=data)


# --> 3 route to fetch and render Car model table
@app.route('/carmodel')
def carmodel_table():

    cursor.execute("SELECT * FROM CarModel")
    data = cursor.fetchall()
    return render_template('view/carModel.html', data=data)


# --> 4 route to fetch and render Car Category table
@app.route('/carcategory')
def carcategory_table():
    
    cursor.execute("SELECT * FROM CarCategory")
    data = cursor.fetchall()
    return render_template('view/carCategory.html', data=data)

# --> 5 route to fetch and render data for CarEngine
@app.route('/carengine')
def carengine_table():

    cursor.execute("SELECT * FROM CarEngine")
    data = cursor.fetchall()
    return render_template('view/carEngine.html', data=data)

# --> 6
@app.route('/carvariant')
def carvariant_table():

    cursor.execute("SELECT * FROM CarVariant")
    data = cursor.fetchall()
    return render_template('view/carVariant.html', data=data)

# --> 7
@app.route('/customer')
def customer_table():

    cursor.execute("SELECT * FROM Customer")
    data = cursor.fetchall()
    return render_template('view/customer.html', data= data)

# --> 8
@app.route('/salesperson')
def display_salesperson():

    cursor.execute("SELECT * FROM SalesPerson")
    data = cursor.fetchall()
    return render_template('view/salesperson.html', data=data)

# --> 9
@app.route('/sale')
def display_sale():

    cursor.execute("SELECT * FROM Sale")
    data = cursor.fetchall()
    return render_template('view/sale.html', data=data)

# --> 10
@app.route('/payment')
def display_payment():
    cursor.execute("SELECT * FROM Payment")
    data = cursor.fetchall()
    return render_template('view/payment.html', data=data)

# --> 11
@app.route('/installment')
def display_installment():

    cursor.execute("SELECT * FROM Installment")
    data = cursor.fetchall()
    return render_template('view/installment.html',data = data)

# --> 12
@app.route('/finance')
def display_finance():

    cursor.execute("SELECT * FROM Finance")
    data = cursor.fetchall()

    return render_template('view/finance.html',data= data)



if __name__ == '__main__':
    app.run(debug=True)
