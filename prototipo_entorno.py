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
    CREATE TABLE IF NOT EXISTS PRODUCTOS (
        id INTEGER PRIMARY KEY,
        BARCODE TEXT,
        ARTICULO TEXT,
        PRECIO REAL
    )
""")

# COMPLETAR: inserten 3 registros de ejemplo con datos realistas de
# su propio sistema (no datos inventados tipo "prueba1", "prueba2")
cursor.executemany(
    "INSERT INTO PRODUCTOS (BARCODE, ARTICULO, PRECIO) VALUES (?, ?, ?)",
    [
        ("457190", "Galletas Mini Barritas Fresa", 30.00),
        ("0044605", "Detergente Roma 1kg", 34.00),
        ("044202", "Atún Nair 120g", 12.00),
    ]
)
conexion.commit()

# Consulta 1: todos los registros
print("--- Todos los registros ---")
for fila in cursor.execute("SELECT * FROM PRODUCTOS"):
    print(fila)

# COMPLETAR: escriban una segunda consulta que filtre por alguna
# condicion relevante a su sistema (usen WHERE)
print("--- Consulta filtrada ---")
for fila in cursor.execute("SELECT * FROM PRODUCTOS WHERE BARCODE == 457190"):
    print(fila)

conexion.close()
