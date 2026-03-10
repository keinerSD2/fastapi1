-- Crear base de datos
CREATE DATABASE neondb;

-- Crear tabla

CREATE TABLE rol (
    id_rol SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    descripcion VARCHAR(50),
    acceso_privilegiado BOOLEAN
);
CREATE TABLE facultad (
    id_facultad SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT
);
CREATE TABLE clinica (
    id_clinica SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    ubicacion VARCHAR(150)
);
CREATE TABLE programa (
    id_programa SERIAL PRIMARY KEY,
    id_facultad INT NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,

    FOREIGN KEY (id_facultad)
        REFERENCES facultad(id_facultad)
);
CREATE TABLE usuario (
    id_usuario SERIAL PRIMARY KEY,
    primer_nombre VARCHAR(50) NOT NULL,
    primer_apellido VARCHAR(50) NOT NULL,
    telefono VARCHAR(20),
    email VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL,
    estado BOOLEAN,
    id_rol INT,

    FOREIGN KEY (id_rol)
        REFERENCES rol(id_rol)
);
CREATE TABLE estudiante (
    id_estudiante SERIAL PRIMARY KEY,
    id_facultad INT,
    id_programa INT,
    id_usuario INT,

    primer_nombre VARCHAR(50) NOT NULL,
    primer_apellido VARCHAR(50) NOT NULL,
    tipo_identificacion VARCHAR(20) NOT NULL,
    numero_identificacion VARCHAR(50) NOT NULL,
    genero VARCHAR(20),
    telefono VARCHAR(20),
    direccion VARCHAR(150),
    fecha_registro TIMESTAMP NOT NULL,

    FOREIGN KEY (id_facultad)
        REFERENCES facultad(id_facultad),

    FOREIGN KEY (id_programa)
        REFERENCES programa(id_programa),

    FOREIGN KEY (id_usuario)
        REFERENCES usuario(id_usuario)
);
CREATE TABLE consulta (
    id_consulta SERIAL PRIMARY KEY,
    id_estudiante INT,
    id_usuario INT,

    diagnostico TEXT,
    observaciones TEXT,
    motivo_consulta TEXT,

    fecha_entrada TIMESTAMP NOT NULL,
    fecha_salida TIMESTAMP NOT NULL,

    FOREIGN KEY (id_estudiante)
        REFERENCES estudiante(id_estudiante),

    FOREIGN KEY (id_usuario)
        REFERENCES usuario(id_usuario)
);
CREATE TABLE signos_vitales (
    id_signos SERIAL PRIMARY KEY,
    id_consulta INT,

    presion_arterial VARCHAR(20),
    temperatura DECIMAL(5,2),
    peso DECIMAL(5,2),
    altura DECIMAL(5,2),
    saturacion_oxigeno DECIMAL(5,2),
    frecuencia_cardiaca INT,
    tipo_sangre VARCHAR(5),

    FOREIGN KEY (id_consulta)
        REFERENCES consulta(id_consulta)
);
CREATE TABLE derivacion (
    id_derivacion SERIAL PRIMARY KEY,
    id_consulta INT,
    id_clinica INT,

    razon TEXT NOT NULL,
    fecha TIMESTAMP,

    FOREIGN KEY (id_consulta)
        REFERENCES consulta(id_consulta),

    FOREIGN KEY (id_clinica)
        REFERENCES clinica(id_clinica)
);
CREATE TABLE emergencia (
    id_emergencia SERIAL PRIMARY KEY,
    id_usuario INT,
    id_estudiante INT,

    fecha TIMESTAMP,
    descripcion TEXT,
    atencion_prestada TEXT,

    FOREIGN KEY (id_usuario)
        REFERENCES usuario(id_usuario),

    FOREIGN KEY (id_estudiante)
        REFERENCES estudiante(id_estudiante)
);

-- Insertar registro

-- ROLES
INSERT INTO rol (nombre, descripcion, acceso_privilegiado) VALUES
('Enfermera', 'Personal de enfermeria', true),
('Administrador', 'Admin del sistema', true),
('Auxiliar', 'Apoyo en enfermeria', false);

-- FACULTADES
INSERT INTO facultad (nombre, descripcion) VALUES
('Ingenieria', 'Facultad de ingenieria'),
('Ciencias de la Salud', 'Facultad de salud'),
('Ciencias Economicas', 'Facultad de economia');

-- CLINICAS
INSERT INTO clinica (nombre, ubicacion) VALUES
('Enfermeria Central', 'Edificio A'),
('Consultorio Norte', 'Bloque B'),
('Area de Emergencias', 'Primer piso');

-- PROGRAMAS
INSERT INTO programa (id_facultad, nombre, descripcion) VALUES
(1, 'Ingenieria de Sistemas', 'Programa de sistemas'),
(2, 'Enfermeria', 'Programa de enfermeria'),
(3, 'Administracion de Empresas', 'Programa administrativo');

-- USUARIOS (enfermeras)
INSERT INTO usuario (primer_nombre, primer_apellido, telefono, email, password, estado, id_rol) VALUES
('Ana', 'Lopez', '3001111111', 'ana@uni.edu', 'pass123', true, 1),
('Maria', 'Perez', '3002222222', 'maria@uni.edu', 'pass123', true, 1),
('Carlos', 'Gomez', '3003333333', 'carlos@uni.edu', 'pass123', true, 2);

-- ESTUDIANTES
INSERT INTO estudiante (id_facultad, id_programa, id_usuario, primer_nombre, primer_apellido, tipo_identificacion, numero_identificacion, genero, telefono, direccion, fecha_registro) VALUES
(1, 1, 1, 'Juan', 'Perez', 'CC', '1001234567', 'Masculino', '3011111111', 'Barranquilla', NOW()),
(2, 2, 2, 'Laura', 'Martinez', 'CC', '1002345678', 'Femenino', '3022222222', 'Soledad', NOW()),
(3, 3, 3, 'Pedro', 'Rodriguez', 'CC', '1003456789', 'Masculino', '3033333333', 'Malambo', NOW());

-- CONSULTAS
INSERT INTO consulta (id_estudiante, id_usuario, diagnostico, observaciones, motivo_consulta, fecha_entrada, fecha_salida) VALUES
(1, 1, 'Dolor de cabeza', 'Paciente estable', 'Dolor fuerte', NOW(), NOW()),
(2, 2, 'Fiebre leve', 'Reposo recomendado', 'Temperatura alta', NOW(), NOW()),
(3, 1, 'Mareo', 'Hidratacion', 'Mareo al levantarse', NOW(), NOW());

-- SIGNOS VITALES
INSERT INTO signos_vitales (id_consulta, presion_arterial, temperatura, peso, altura, saturacion_oxigeno, frecuencia_cardiaca, tipo_sangre) VALUES
(1, '120/80', 36.5, 70, 1.75, 98, 75, 'O+'),
(2, '110/70', 38.2, 65, 1.68, 97, 80, 'A+'),
(3, '115/75', 36.8, 80, 1.80, 99, 72, 'B+');

-- DERIVACIONES
INSERT INTO derivacion (id_consulta, id_clinica, razon, fecha) VALUES
(1, 1, 'Revision general', NOW()),
(2, 3, 'Evaluacion por emergencia', NOW()),
(3, 2, 'Consulta especializada', NOW());

-- EMERGENCIAS
INSERT INTO emergencia (id_usuario, id_estudiante, fecha, descripcion, atencion_prestada) VALUES
(1, 1, NOW(), 'Desmayo en clase', 'Se estabilizo y reposo'),
(2, 2, NOW(), 'Fiebre alta', 'Control de temperatura'),
(1, 3, NOW(), 'Dolor abdominal fuerte', 'Observacion y derivacion');
