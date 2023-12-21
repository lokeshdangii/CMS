#!/bin/bash

echo "Step 1: Installation"
sudo apt update -y > /dev/null
sudo apt-get remove needrestart -y
sudo apt-get install python3-venv -y > /dev/null
sudo apt install mysql-server -y
echo "Installation completed successfully."

echo "Step 2: Setting Up Application"
git clone https://github.com/lokeshdangii/CMS
cd CMS/
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
echo "Application setup completed successfully."

echo "Step 3: Setting up database"
sudo mysql -e "CREATE DATABASE cardb;"
sudo mysql cardb < cardb.sql
sudo mysql -e "ALTER USER 'root'@'localhost' IDENTIFIED with mysql_native_password By 'root';" 
echo "Database setup completed successfully."

echo "Running the CMS application"
python3 app.py