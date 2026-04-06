CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    user_id INT,
    title TEXT,
    status TEXT
);

CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    user_id INT,
    title TEXT,
    datetime TIMESTAMP
);

CREATE TABLE notes (
    id SERIAL PRIMARY KEY,
    user_id INT,
    content TEXT
);

CREATE TABLE user_preferences (
    id SERIAL PRIMARY KEY,
    user_id INT,
    key TEXT,
    value TEXT
);