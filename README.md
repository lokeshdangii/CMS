# CMS Application

The CMS (Car Management System) Application is a web-based system designed to manage car-related data and specifications. This application allows users to perform Create, Read, Update, and Delete (CRUD) operations on various car-related data components and specification. Here's a comprehensive guide on using the CMS Application.

## Table of Contents

1. [Introduction](#introduction)
2. [Technology Stack](#technology-stack)
3. [Project Structure](#project-structure)
4. [Prerequisites](#prerequisites)
5. [Installation](#installation)
6. [Database Initialization and Configuration](#database-initialization-and-configuration)
7. [Running the Application](#running-the-application)
8. [Functionalities](#functionalities)

## Introduction

The CMS Application simplifies car data management by offering an intuitive web-based interface. Users can effortlessly perform CRUD operations on the following key components:

- Car Colors
- Car Categories
- Car Models
- Car Variants
- Car Engines
- Cars

This application ensures that car-related data can be easily viewed, added, edited, or deleted, with an added layer of security through user authentication.

## Technology Stack

### Frontend

- HTML
- CSS

### Backend

- Python
- Flask (Web Framework)
- MySQL (Database)

## Project Structure

The project directory includes the following files and directories:

- `app.py`: The main application file that initializes the Flask instance and connects various functionalities using Blueprints.
- `auth.py`: Responsible for user authentication and authorization.
- `car.py`: Contains logic and views for CRUD operations related to Cars.
- `car_category.py`: Manages CRUD operations for Car Categories.
- `car_color.py`: Handles CRUD operations for Car Colors.
- `car_engine.py`: Manages CRUD operations for Car Engines.
- `car_model.py`: Manages CRUD operations for Car Models.
- `car_variant.py`: Handles CRUD operations for Car Variants.
- `cardb.sql`: An SQL script for initializing the database schema.
- `db.py`: Configures the database for the project.

##### Directory 
- `templates` : This directory contain all the HTML files.
- `static` : This directory contain CSS and image files.

## Prerequisites

Before proceeding with the installation and execution of the application, ensure you have the following dependencies installed on your system:

- Python 3.x
- Git
- MySQL server installed and running.

## Installation

1. Clone the GitHub repository to your desired location:

   ```bash
   git clone https://github.com/lokeshdangii/CMS
   ```

2. Navigate to the "CMS" directory:

   ```bash
   cd CMS
   ```

3. Install the required packages and libraries by executing:

   ```bash
   pip install -r requirements.txt
   ```

## Database Initialization and Configuration

Before running the application, it's essential to initialize the database and configure the connection. Follow these steps:

1. Import the database schema by running the SQL script (`cardb.sql`) provided in the repository. This script will set up the required tables and initial data.

2. Update the MySQL database configuration in the `db.py` file. Open `db.py` and provide your MySQL database connection details as follows:

   ```python
   db_config = {
       "host": "your_database_host",
       "user": "your_database_user",
       "password": "your_database_password",
       "database": "your_database_name"
   }
   ```

   Save the changes.

## Running the Application

To launch the application, execute the following command:

```bash
flask --app app.py run
```

This command will start the Flask development server, and you can access the CMS Application in your web browser at http://localhost:5000.

## Functionalities

The CMS Application offers the following essential functionalities:

1. Manage Car Colors
2. Manage Car Categories
3. Manage Car Models
4. Manage Car Variants
5. Manage Car Engines
6. Manage Cars

Users can effortlessly perform CRUD operations on these components, enabling them to add, view, update, or delete entries as necessary.

With the CMS Application, efficient car data management is just a few clicks away. Ensure you've completed the database initialization and configuration steps for a seamless user experience.