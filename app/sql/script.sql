-- Crear base de datos
CREATE DATABASE prueba;


-- Crear tabla
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL,
    apellido VARCHAR(20) NOT NULL,
    cedula VARCHAR(20) NOT NULL,
    edad INTEGER NOT NULL,
    usuario VARCHAR(20) NOT NULL,
    contrasena VARCHAR(20) NOT NULL
);

CREATE TABLE tipo_documento (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    descripcion TEXT
);


CREATE TABLE cliente (
    id SERIAL PRIMARY KEY,
    primer_nombre VARCHAR(100) NOT NULL,
    segundo_nombre VARCHAR(100),
    primer_apellido VARCHAR(100) NOT NULL,
    segundo_apellido VARCHAR(100),
    numero_documento VARCHAR(50) NOT NULL,
    correo VARCHAR(100),
    telefono VARCHAR(20),
    tipo_documento_id INT NOT NULL,

    CONSTRAINT fk_tipo_documento
        FOREIGN KEY (tipo_documento_id)
        REFERENCES tipo_documento(id)
);

-- Pruebas
INSERT INTO usuarios (nombre, apellido, cedula, edad, usuario, contrasena)
VALUES ('pedro', 'perez', '10102020', 30, 'pperez', '12345');

INSERT INTO tipo_documento (nombre, descripcion)
VALUES ('Cedula', 'Documento nacional');

INSERT INTO cliente
(primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, numero_documento, correo, telefono, tipo_documento_id)
VALUES
('Camila', 'Andrea', 'Caceres', 'Reyes', '123456', 'camila@email.com', '3001234567', 1);
