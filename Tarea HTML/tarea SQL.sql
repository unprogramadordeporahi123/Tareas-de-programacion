CREATE TABLE Compas (
    cedula INT PRIMARY KEY,
    primer_nombre VARCHAR(100),
    apellido VARCHAR(100),
    edad INT,
    pelicula_favorita VARCHAR(100)
);

INSERT INTO Compas (cedula, primer_nombre, apellido, edad, pelicula_favorita) VALUES
(3493845, 'Manolo', 'Perez', 15, 'Spiderman'),
(12128461, 'Peter', 'Parker', 18, 'Venom'),
(12421467, 'Victor', 'Vilchez', 17, 'Batman'),
(12654124, 'Picoro', 'Daimaku', 30, 'Dragon Ball Super: Super Hero');

ALTER TABLE Compas
ADD COLUMN Transformacion VARCHAR(100);

DROP TABLE Shippings

UPDATE Compas
SET pelicula_favorita = 'Dragon Ball Z: El Legendario Super Sayajin'
WHERE cedula = 12654124;

SELECT * FROM Compas;

SELECT cedula, primer_nombre, apellido, edad FROM Compas;

SELECT * FROM Compas WHERE pelicula_favorita = 'Dragon Ball Z: El Legendario Super Sayajin';

SELECT * FROM Compas WHERE age > 30;

SELECT * FROM Compas ORDER BY edad ASC;

SELECT COUNT(*) FROM Customers;

SELECT SUM(edad) FROM Compas;