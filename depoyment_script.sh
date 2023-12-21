
#!/bin/bash

# Script to deploy and Serve CMS Application with uWSGI and Nginx on Ubuntu

echo "Step 1: Installation"
sudo apt update -y > /dev/null
sudo apt-get remove needrestart -y
sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools -y
sudo apt-get install python3-venv -y > /dev/null
sudo apt install mysql-server -y
echo "Installation completed successfully."

echo "Step 2: Setting Up Application"
cd /home/ubuntu
git clone https://github.com/lokeshdangii/CMS
cd CMS/
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
pip install wheel
pip install uwsgi flask
echo "Application setup completed successfully."

echo "Step 3: Setting up database"
sudo mysql -e "CREATE DATABASE cardb;"
sudo mysql cardb < cardb.sql
sudo mysql -e "ALTER USER 'root'@'localhost' IDENTIFIED with mysql_native_password By 'root';" 
echo "Database setup completed successfully."

echo "Running the CMS application"
# python3 app.py

# deactivate the virtual environment env
deactivate

# systemd unit file --> cms.service
sudo cp cms.service /etc/systemd/system/

# changing the group associated with home directory because the Nginx www-data user won’t be able to read files in your home directory by default
sudo chgrp www-data /home/ubuntu

# start the uWSGI created service --> cms.service :
sudo systemctl start cms

# enable it so that it starts at boot:
sudo systemctl enable cms

# Check the status:
echo "-------------------- status of CMS Service --------------------------------------"
sudo systemctl status cms

# Installing nginx
sudo apt install nginx -y

# Configuring Nginx to Proxy Requests
sudo cp cms /etc/nginx/sites-available/

# To enable the Nginx server block configuration you’ve just created,
# link the file to the sites-enabled directory:

sudo ln -s /etc/nginx/sites-available/cms /etc/nginx/sites-enabled

# unlink the default one
sudo unlink /etc/nginx/sites-enabled/default

# restart the Nginx process to read the new configuration:
sudo systemctl restart nginx

# adjust the firewall once again
sudo ufw delete allow 5000
sudo ufw allow 'Nginx Full'

echo "Your Application is deployed successfully"
echo "Access your application by the IP Address"