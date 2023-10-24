import requests
import sqlite3
from forex_python.converter import CurrencyRates
from datetime import date


def obtener_precio_bitcoin():
    try:
        url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
        response = requests.get(url)
        response.raise_for_status()  

        data = response.json()
        precio_bitcoin = data["bpi"]["USD"]["rate_float"]

        return precio_bitcoin

    except requests.RequestException as e:
        print(f"Error al obtener el precio de Bitcoin: {e}")
        return None

def crear_tabla_bitcoin():
    try:
        conn = sqlite3.connect('base.db')
        cursor = conn.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS bitcoin (
            fecha TEXT,
            precio_usd REAL,
            precio_gbp REAL,
            precio_eur REAL,
            precio_pen REAL
        )
        ''')

        conn.commit()
        conn.close()
        print("Tabla 'bitcoin' creada con éxito.")
    except Exception as e:
        print(f"Error al crear la tabla 'bitcoin': {e}")

def insertar_datos_bitcoin(fecha, precio_usd, precio_gbp, precio_eur, precio_pen):
    try:
        conn = sqlite3.connect('base.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO bitcoin (fecha, precio_usd, precio_gbp, precio_eur, precio_pen) VALUES (?, ?, ?, ?, ?)",
                    (fecha, precio_usd, precio_gbp, precio_eur, precio_pen))

        conn.commit()
        conn.close()
        print("Datos de Bitcoin insertados con éxito.")
    except Exception as e:
        print(f"Error al insertar datos en la tabla 'bitcoin': {e}")

def calcular_precio_compra_10_bitcoins():
    fecha = date.today()
    precio_usd = obtener_precio_bitcoin()
    
    if precio_usd is not None:
        cantidad_bitcoins = 10
        precio_pen = obtener_tipo_cambio_pen() * precio_usd
        precio_eur = obtener_tipo_cambio_eur() * precio_usd

        costo_compra_pen = cantidad_bitcoins * precio_pen
        costo_compra_eur = cantidad_bitcoins * precio_eur

        insertar_datos_bitcoin(fecha, precio_usd, precio_usd, precio_usd, precio_pen)
        
        print(f"Precio de compra de 10 Bitcoins en PEN: {costo_compra_pen:.4f}")
        print(f"Precio de compra de 10 Bitcoins en EUR: {costo_compra_eur:.4f}")
    else:
        print("No se pudo obtener el precio de Bitcoin.")

def obtener_tipo_cambio_pen():
    try:
        c = CurrencyRates()
        return c.get_rate('USD', 'PEN')
    except Exception as e:
        print(f"Error al obtener el tipo de cambio de PEN: {e}")
        return None

def obtener_tipo_cambio_eur():
    try:
        c = CurrencyRates()
        return c.get_rate('USD', 'EUR')
    except Exception as e:
        print(f"Error al obtener el tipo de cambio de EUR: {e}")
        return None

if __name__ == "__main__":
    crear_tabla_bitcoin()
    try:
        calcular_precio_compra_10_bitcoins()
    except FileNotFoundError:
        print(f" Hubo un error al ejecutar la funcion calcular_precio_compra_10_bitcoin")
