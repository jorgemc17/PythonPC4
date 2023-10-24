import requests
import sqlite3

conn = sqlite3.connect("base.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sunat_info (
    fecha TEXT,
    compra REAL,
    venta REAL
)
""")

for month in range(1, 13): 
    url = f'https://api.apis.net.pe/v1/tipo-cambio-sunat?month={month}&year=2023'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        for registro in data:
            fecha = registro['fecha']
            compra = registro['compra']
            venta = registro['venta']
            cursor.execute("INSERT INTO sunat_info (fecha, compra, venta) VALUES (?, ?, ?)", (fecha, compra, venta))

conn.commit()
conn.close()

conn = sqlite3.connect("base.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM sunat_info")
for row in cursor.fetchall():
    print(row)

conn.close()

