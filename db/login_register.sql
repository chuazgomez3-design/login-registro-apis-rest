/* =========================================
   CREAR BASE DE DATOS
========================================= */
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'login_registro')
BEGIN
    CREATE DATABASE login_registro;
END
GO

USE login_registro;
GO

/* =========================================
   TABLA USUARIOS
========================================= */
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'usuarios')
BEGIN
    CREATE TABLE usuarios(
        id_usuario INT IDENTITY(1,1) PRIMARY KEY,
        nombre_usuario VARCHAR(100) NOT NULL UNIQUE,
        correo_usuario VARCHAR(150) NOT NULL UNIQUE,
        password_usuario VARCHAR(255) NOT NULL,
        activo BIT DEFAULT 1,
        fecha_creacion DATETIME2 DEFAULT GETDATE()
    );
END
GO

/* =========================================
   ÍNDICES (MEJOR RENDIMIENTO)
========================================= */
IF NOT EXISTS (SELECT name FROM sys.indexes WHERE name = 'idx_usuario')
BEGIN
    CREATE INDEX idx_usuario ON usuarios(nombre_usuario);
END
GO

IF NOT EXISTS (SELECT name FROM sys.indexes WHERE name = 'idx_correo')
BEGIN
    CREATE INDEX idx_correo ON usuarios(correo_usuario);
END
GO

/* =========================================
   VALIDACIÓN (NO DUPLICADOS)
========================================= */
-- Ya cubierto con UNIQUE

/* =========================================
   DATOS DE PRUEBA
========================================= */
IF NOT EXISTS (SELECT * FROM usuarios WHERE nombre_usuario = 'admin')
BEGIN
    INSERT INTO usuarios (nombre_usuario, correo_usuario, password_usuario)
    VALUES ('admin', 'admin@gmail.com', '123456');
END
GO

/* =========================================
   CONSULTAS ÚTILES
========================================= */

-- Ver usuarios
SELECT * FROM usuarios;

-- Buscar usuario por login
-- (lo que usa tu API)
-- SELECT * FROM usuarios WHERE nombre_usuario = 'admin' AND password_usuario = '123456';

-- Eliminar usuario (prueba)
-- DELETE FROM usuarios WHERE id_usuario = 1;