CREATE TABLE movies (
    film_id INTEGER PRIMARY KEY AUTOINCREMENT,
    movie_title VARCHAR(30),
    genre CHAR(3),
    third_dimension_film BOOLEAN
);

CREATE TABLE tickets (
    ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
    film_id INTEGER,
    number_tickets INTEGER,
    ticket_name VARCHAR(40),
    FOREIGN KEY(film_id) REFERENCES movies(film_id)
);