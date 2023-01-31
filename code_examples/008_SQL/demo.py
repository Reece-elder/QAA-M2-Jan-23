# Sqlite is an embedded local DB, that is installed in Python by default
import sqlite3 as sql

# Creating a connection object, by running the connect() function
conn = sql.connect("new-db") # If this file doesn't exist, create it. If it does, connect to it

# Making a cursor running the cursor() function that belongs to our conn object
cursor = conn.cursor()

# Reading our sql file
def creatingTable():
    sql_file = open("cinema.sql")
    sql_string = sql_file.read()
    # print(sql_string)
    # Running our sql command using our cursor
    cursor.executescript(sql_string)

# creatingTable() 

print(cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall())

# Within SQL you get two types of queries 
# Data Manipulation Queries (Creating, Updating or Deleting Data)
# Data Selection Queries (Getting data)

def addData():
    # query = "INSERT INTO <table name> (field_1, field_2, field_3) VALUES ('value_1', value_2, value_3);"
    movie_query = "INSERT INTO movies (movie_title, genre, third_dimension_film) VALUES ('shrek 1', 'COM', true);"
    ticket_query = "INSERT INTO tickets (film_id, number_tickets, ticket_name) VALUES (1, 4, 'Wesley Snipes');"

    cursor.execute(movie_query)
    cursor.execute(ticket_query)

    select_query = "SELECT * FROM movies" # Reading data from DBs, SELECT * what columns to see, 
    # cursor selects the data, fetchAll() imports it to python
    print(cursor.execute(select_query).fetchall())
    print(cursor.execute("SELECT * FROM tickets").fetchall())

addData()

# Saves your changes to the DB
conn.commit()