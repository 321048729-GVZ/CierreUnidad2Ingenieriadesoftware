"""
Prototipo minimo de entorno -- Cierre de Unidad 2
Ingenieria de Software . Grupo 1359 / 1359A

Completen cada linea marcada con # COMPLETAR usando informacion real
de su sistema. No dejen texto de ejemplo ("prueba1", "dato1", etc.).
"""

import sqlite3

conexion = sqlite3.connect("prototipo.db")
cursor = conexion.cursor()

# COMPLETAR: nombren la tabla segun el objeto central de su sistema,
# y definan 3 o 4 columnas relevantes (ademas de id)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS NOMBRE_TABLA (
        id INTEGER PRIMARY KEY,
        COLUMNA_1 TEXT,
        COLUMNA_2 TEXT,
        COLUMNA_3 TEXT
    )
""")

# COMPLETAR: inserten 3 registros de ejemplo con datos realistas de
# su propio sistema (no datos inventados tipo "prueba1", "prueba2")
cursor.executemany(
    "INSERT INTO NOMBRE_TABLA (COLUMNA_1, COLUMNA_2, COLUMNA_3) VALUES (?, ?, ?)",
    [
        ("VALOR_1", "VALOR_2", "VALOR_3"),
        ("VALOR_1", "VALOR_2", "VALOR_3"),
        ("VALOR_1", "VALOR_2", "VALOR_3"),
    ]
)
conexion.commit()

# Consulta 1: todos los registros
print("--- Todos los registros ---")
for fila in cursor.execute("SELECT * FROM NOMBRE_TABLA"):
    print(fila)

# COMPLETAR: escriban una segunda consulta que filtre por alguna
# condicion relevante a su sistema (usen WHERE)
print("--- Consulta filtrada ---")
for fila in cursor.execute("SELECT * FROM NOMBRE_TABLA WHERE CONDICION"):
    print(fila)

conexion.close()
