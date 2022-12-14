PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS files;

CREATE TABLE files (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename VARCHAR(64) NOT NULL,
    origname VARCHAR(64) NOT NULL,
    duration INTEGER NOT NULL,
    filetype VARCHAR(64) NOT NULL,
    uploaded DATETIME DEFAULT CURRENT_TIMESTAMP
);