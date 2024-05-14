# Install MySQL
# run pip install mysql
# run pip install mysql-connector or pip install mysql-connector-python

import mysql
import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',

)

# Prepare cursor object
cursorObject = dataBase.cursor()

# Create database
cursorObject.execute("CREATE DATABASE finances")

print("Database created")