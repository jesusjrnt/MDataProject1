CREATE TABLE IF NOT EXISTS Equilibrio_discapacidad (
    id_equilibrio_discapacidad INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario CHAR(4),
    d_movilidad INT,
    d_aprendizaje INT,
    d_comunicacion INT,
    d_relaciones_sociales INT,
    d_autocuidado INT,
    d_vision INT,
    d_audicion INT,
    d_vida_domestica INT
);

CREATE TABLE IF NOT EXISTS Esperanza_de_vida (
    id_esperanza_de_vida INT AUTO_INCREMENT PRIMARY KEY,
    id_provincia INT,
    provincia TEXT,
    sexo TEXT,
    edad_en_dias INT,
    enfermedad_terminal_en_dias INT
);

CREATE TABLE IF NOT EXISTS Diferencia_fechas_viajes (
    id_diferencia_fechas_viajes INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario CHAR(4),
    fecha_ultimo_viaje DATE
);

CREATE TABLE IF NOT EXISTS Compromiso_usuario (
    id_compromiso_usuario INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario CHAR(4),
    valoracion_usuario INT,
    fecha_cancelacion DATE
); 

CREATE TABLE IF NOT EXISTS Promocion_Movilidad (
    id_promocion_movilidad INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario CHAR(4),
    id_provincia INT
);

CREATE TABLE IF NOT EXISTS Tipo_de_viaje (
    id_tipo_de_viaje INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario CHAR(4),
    tipo_viaje_1 TEXT,
    tipo_viaje_2 TEXT,
    tipo_viaje_3 TEXT,
    tipo_viaje_4 TEXT,
    tipo_viaje_5 TEXT

);

CREATE TABLE IF NOT EXISTS Proximo_viaje (
    id_proximo_viaje INT AUTO_INCREMENT PRIMARY KEY,
    id_provincia INT,
    provincia TEXT,
    plazas_disponibles INT,
    tipo_de_viaje TEXT
);