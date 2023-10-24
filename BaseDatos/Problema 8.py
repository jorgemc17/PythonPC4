import sqlite3
import requests
from datetime import date
import json

# Crear una conexión a la base de datos (o crear una nueva base de datos si no existe)
conn = sqlite3.connect('base.db')
cursor = conn.cursor()

# Crear la tabla 'bitcoin' si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS bitcoin (
    fecha TEXT,
    precio_usd REAL,
    precio_gbp REAL,
    precio_eur REAL,
    precio_pen REAL
)
''')

# Confirmar y cerrar la conexión a la base de datos
conn.commit()
conn.close()

def obtener_precio_bitcoin():
    try:
        url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
        response = requests.get(url)
        response.raise_for_status()  

        data = response.json()
        precio_usd = data["bpi"]["USD"]["rate_float"]
        precio_gbp = data["bpi"]["GBP"]["rate_float"]
        precio_eur = data["bpi"]["EUR"]["rate_float"]

        # Consultar la API de SUNAT para obtener el tipo de cambio de PEN (reemplaza con la URL correcta)
        url_sunat = 'https://api.apis.net.pe/v1/tipo-cambio-sunat?month=10&year=2023'
        response = requests.get(url_sunat)
        tipo_cambio_pen = None

        if response.status_code == 200:
            # La respuesta de la API de SUNAT es una lista, por lo que necesitamos extraer el valor
            data = json.loads(response.text)
            if len(data) > 0:
                tipo_cambio_pen = data[0].get('valorVenta')

        if tipo_cambio_pen is not None:
            # Obtener la fecha actual
            fecha_actual = date.today()

            # Crear una conexión a la base de datos
            conn = sqlite3.connect('base.db')
            cursor = conn.cursor()

            # Insertar los datos en la tabla 'bitcoin' con la fecha actual
            cursor.execute("INSERT INTO bitcoin (fecha, precio_usd, precio_gbp, precio_eur, precio_pen) VALUES (?, ?, ?, ?, ?)",
                           (fecha_actual, precio_usd, precio_gbp, precio_eur, tipo_cambio_pen * precio_usd))

            # Confirmar y cerrar la conexión a la base de datos
            conn.commit()
            conn.close()

            return fecha_actual
        else:
            print("Error al obtener el tipo de cambio de PEN desde la API de SUNAT.")
            return None

    except requests.RequestException as e:
        print(f"Error al obtener el precio de Bitcoin: {e}")
        return None

def calcular_precio_compra_10_bitcoins():
    fecha = obtener_precio_bitcoin()

    if fecha:
        conn = sqlite3.connect('base.db')
        cursor = conn.cursor()
        cursor.execute("SELECT precio_usd, precio_eur, precio_pen FROM bitcoin WHERE fecha = ?", (fecha,))
        row = cursor.fetchone()
        conn.close()

        if row:
            precio_usd = row[0]
            precio_eur = row[1]
            precio_pen = row[2]

            cantidad_bitcoins = 10
            precio_compra_pen = cantidad_bitcoins * precio_pen
            precio_compra_eur = cantidad_bitcoins * precio_eur

            print(f"Precio de compra de 10 Bitcoins en PEN: {precio_compra_pen:.4f}")
            print(f"Precio de compra de 10 Bitcoins en EUR: {precio_compra_eur:.4f}")
        else:
            print("No se encontraron datos en la tabla 'bitcoin' para la fecha actual.")
    else:
        print("No se pudieron obtener los datos del precio de Bitcoin.")

if __name__ == "__main__":
    calcular_precio_compra_10_bitcoins()

