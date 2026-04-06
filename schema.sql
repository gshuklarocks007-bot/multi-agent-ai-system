CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
);

CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    title TEXT,
    status TEXT
);

CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    title TEXT,
    datetime TEXT
);

CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    content TEXT
);

CREATE TABLE IF NOT EXISTS user_preferences (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    key TEXT,
    value TEXT
);

-- Sample Data
INSERT INTO users (name) VALUES ('Gaurav');

INSERT INTO tasks (user_id, title, status)
VALUES
(1, 'Finish project report', 'pending'),
(1, 'Prepare presentation', 'pending');

INSERT INTO events (user_id, title, datetime)
VALUES
(1, 'Team Meeting', '2026-04-06 10:00');

INSERT INTO notes (user_id, content)
VALUES
(1, 'Discuss milestones');