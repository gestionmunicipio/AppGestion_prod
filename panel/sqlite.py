# Importar módulo
import sqlite3
from sqlite3.dbapi2 import Cursor

# Conexión
conexion = sqlite3.connect('db8PE.db')

# Crear Cursor
cursor = conexion.cursor()

# Crea tabla de proceso de diagnóstico
cursor.execute ("""
CREATE TABLE IF NOT EXISTS tb_proceso(
    idproceso INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario VARCHAR(50) NOT NULL,
    fecha DATETIME NOT NULL
);
""")

conexion.commit()

# Insertar registros
cursor.execute ("INSERT INTO tb_proceso VALUES (null, 'Prueba 1', '28-06-2021 13:43');")
conexion.commit()

# Desplegar registros
cursor.execute ("SELECT * FROM tb_proceso;")
registros = cursor.fetchall()

for proceso in registros:
    print(registros)


# Cerrar conexión
conexion.close()

