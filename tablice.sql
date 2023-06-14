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

CREATE TABLE svirka (
id_svirke INTEGER PRIMARY KEY AUTOINCREMENT,
datum DATE NOT NULL,
opis CHAR(50),
cijena INTEGER
);

CREATE TABLE blagajna (
id_racuna INTEGER PRIMARY KEY AUTOINCREMENT,
blagajna INTEGER,
ukupna_zarada INTEGER
);

INSERT INTO instrument (naziv) VALUES
    ('Prim'),
    ('Basprim'),
    ('Harmonika'),
    ('Bas'),
    ('Bugarija'),
    ('Bubanj');