CREATE TABLE clan (
id_clana INTEGER PRIMARY KEY AUTOINCREMENT,
ime CHAR(50) NOT NULL,
prezime CHAR(50) NOT NULL,
id_instrumenta TINYINT
);

CREATE TABLE instrument (
id INTEGER PRIMARY KEY AUTOINCREMENT,
naziv CHAR(50) NOT NULL
);


INSERT INTO instrument (naziv) VALUES
    ('Prim'),
    ('Basprim'),
    ('Harmonika'),
    ('Bas'),
    ('Bugarija'),
    ('Bubanj');