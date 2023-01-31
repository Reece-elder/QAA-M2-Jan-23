# Sqlite is an embedded local DB, that is installed in Python by default
import sqlite3 as sql

# Creating a connection object, by running the connect() function
conn = sql.connect("new-db") # If this file doesn't exist, create it. If it does, connect to it

# Making a cursor running the cursor() function that belongs to our conn object
cursor = conn.cursor()

# Reading our sql file
sql_file = open("cinema.sql")
sql_string = sql_file.read()
# print(sql_string)
# Running our sql command using our cursor
cursor.executescript(sql_string)