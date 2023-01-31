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

INSERT INTO movies (movie_title, genre, third_dimension_film) VALUES ('Movie 1', 'HOR', true);
INSERT INTO movies (movie_title, genre, third_dimension_film) VALUES ('Movie 2', 'COM', false);
INSERT INTO movies (movie_title, genre, third_dimension_film) VALUES ('Movie 3', 'ACT', true);

INSERT INTO tickets (film_id, number_tickets, ticket_name) VALUES (1, 4, 'Wesley Snipes');
INSERT INTO tickets (film_id, number_tickets, ticket_name) VALUES (2, 3, 'Kate Beckinsdale');
INSERT INTO tickets (film_id, number_tickets, ticket_name) VALUES (1, 6, 'Milla Jovovich');
