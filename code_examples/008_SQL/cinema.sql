-- enclosures and animals
-- both tables must include a primary key and atleast 4 variables (excluding primary key)
-- animals must belong to an enclosure 

-- two dashes to make an SQL comment, SQL reads top to bottom just like python 

-- 
CREATE TABLE movies (
    film_id INTEGER AUTOINCREMENT PRIMARY KEY,
    title VARCHAR(30),
    genre CHAR(3),
    3D_film BOOLEAN
);

CREATE TABLE tickets (
    ticket_id INTEGER AUTOINCREMENT PRIMARY KEY,
    film_id INTEGER,
    number_tickets INTEGER,
    ticket_name VARCHAR(40),
    FOREIGN KEY(film_id) REFERENCES movies(film_id)
);