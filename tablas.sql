CREATE TABLE IF NOT EXISTS tabla_equilibrio_discapacidad (
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

CREATE TABLE IF NOT EXISTS tabla_esperanza_de_vida_provincia_sexo (
    id_esperanza_de_vida_provincia_sexo INT AUTO_INCREMENT PRIMARY KEY,
    id_provincia INT,
    provincia TEXT,
    hombres TEXT,
    mujeres TEXT
);

CREATE TABLE IF NOT EXISTS tabla_edad_sexo (
    id_edad_sexo INT AUTO_INCREMENT PRIMARY KEY,
    id_provincia INT,
    sexo TEXT,
    edad_en_dias INT,
    enfermedad_terminal_en_dias INT
);

CREATE TABLE IF NOT EXISTS tabla_diferencia_fechas_viajes (
    id_diferencia_fechas_viajes INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario CHAR(4),
    fecha_ultimo_viaje DATE,
    fecha_hoy DATE
);

CREATE TABLE IF NOT EXISTS tabla_compromiso_usuario (
    id_compromiso_usuario INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario CHAR(4),
    valoracion_usuario INT,
    fecha_cancelacion DATE
); 

CREATE TABLE IF NOT EXISTS tabla_promocion_movilidad (
    id_promocion_movilidad INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario CHAR(4),
    id_provincia INT,
    provincia TEXT
);

CREATE TABLE IF NOT EXISTS tabla_tipo_de_viaje (
    id_tipo_de_viaje INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario CHAR(4),
    tipo_viaje_1 TEXT,
    tipo_viaje_2 TEXT,
    tipo_viaje_3 TEXT,
    tipo_viaje_4 TEXT

);

CREATE TABLE IF NOT EXISTS tabla_proximo_viaje (
    id_proximo_viaje INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario CHAR(4),
    id_provincia_proximo_viaje INT,
    provincia_proximo_viaje TEXT,
    plazas_disponibles INT,
    tipo_de_viaje TEXT
);

CREATE TABLE IF NOT EXISTS tabla_puntos (
    id_puntos INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario CHAR(4),
    puntos_discapacidad INT,
    puntos_esperanza INT,
    puntos_diferencia_viajes INT,
    puntos_compromiso INT
);