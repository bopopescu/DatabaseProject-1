# insert your password wherever it says "your_password"

import mysql.connector
from DBandTables.ConnectionToDB import DatabaseConnection

mydb = DatabaseConnection()
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE UYPdb")