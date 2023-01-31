# Sqlite is an embedded local DB, that is installed in Python by default
import sqlite3 as sql

# Creating a connection object, by running the connect() function
conn = sql.connect("new-db") # If this file doesn't exist, create it. If it does, connect to it

conn.execute("PRAGMA foreign_keys = 1") # forces Foreign Key restraints 

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

def insertMovie():
    movie_title = input("Please enter movie title: ")
    # query = "INSERT INTO <table name> (field_1, field_2, field_3) VALUES ('value_1', value_2, value_3);"
    movie_query = f"INSERT INTO movies (movie_title, genre, third_dimension_film) VALUES ('{movie_title}', 'HOR', true);"
    cursor.execute(movie_query)
    return True

def insertTicket(film_id):
    # query = "INSERT INTO <table name> (field_1, field_2, field_3) VALUES ('value_1', value_2, value_3);"
    ticket_query = f"INSERT INTO tickets (film_id, number_tickets, ticket_name) VALUES ({film_id}, 5, 'Wesley Snipes');"
    cursor.execute(ticket_query)
    return True

def readAllData(table_name):
    select_query = f"SELECT * FROM {table_name}"
    return cursor.execute(select_query).fetchall()

def readAllMoviesGenre(genre):
    query = f"SELECT * FROM movies WHERE genre='{genre}'"
    return cursor.execute(query).fetchall()

def readAllQuery(query):
    return cursor.execute(query).fetchall()

def readMovieId():
    film_id = input("Please choose ID: ")
    query = f"SELECT * FROM movies WHERE film_id = {film_id}"
    return readAllQuery(query)

# insertMovie()
# insertTicket(1)
# insertTicket(2)
# insertTicket(3)
# insertTicket(12)
# print(readAllMoviesGenre("HOR"))
# print(readAllData("movies"))
# print(readAllQuery("SELECT * FROM tickets WHERE number_tickets < 4"))
# insertMovie()
# print(insertTicket(500))
print(readMovieId())

# Exercise - Implement a function that gets an animal by animal id (pass in id)
# Create a function that gets all records from one condition the user can set (pass in field and value)

# Saves your changes to the DB
conn.commit()