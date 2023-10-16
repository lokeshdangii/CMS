import mysql.connector


# Database configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "newcardb2"
}

# Create a connection to the MySQL database
db = mysql.connector.connect(**db_config)

# Initialize a cursor
cursor = db.cursor()