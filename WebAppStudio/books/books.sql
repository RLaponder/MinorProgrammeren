CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    isbn VARCHAR UNIQUE NOT NULL,
    title VARCHAR NOT NULL,
    author VARCHAR NOT NULL,
    year INTEGER NOT NULL
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    email VARCHAR UNIQUE NOT NULL,
    password VARCHAR NOT NULL
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    book_id INTEGER REFERENCES books,
    rating INTEGER NOT NULL CONSTRAINT Invalid_Rating CHECK (rating <=5 AND rating>=1),
    written_review VARCHAR
);