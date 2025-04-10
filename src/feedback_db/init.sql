CREATE DATABASE feedback;

\c feedback;

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    text TEXT
);
