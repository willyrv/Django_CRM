# Install Mysql on your computer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'django',
    passwd = 'DjangoAdmin*12345'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
#cursorObject.execute("CREATE DATABASE djangocrmdb")
cursorObject.execute("SHOW DATABASES")

