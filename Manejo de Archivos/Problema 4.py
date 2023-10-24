""" Almacene los datos de precio de Bitcoin en un archivo txt con un 
formato que consideré apropiado. """
import requests

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    precio_bitcoin = data['bpi']['USD']['rate']

    formato_datos = f'Precio de Bitcoin en USD: {precio_bitcoin}\n'

    este_archivo = 'bitcoin_price.txt'

    with open(este_archivo, 'w') as archivo:
        archivo.write(formato_datos)

    print(f'Los datos se han guardado en {este_archivo}.')
else:
    print("Error al obtener datos de la API de CoinDesk.")

este_archivo = 'bitcoin_price.txt'

try:
    with open(este_archivo, 'r') as archivo:
        contenido = archivo.read()
        print("Contenido del archivo 'bitcoin_price.txt':")
        print(contenido)
except FileNotFoundError:
    print(f"El archivo '{este_archivo}' no existe o no se ha guardado aún.")
except Exception as e:
    print(f"Error al leer el archivo: {e}")
