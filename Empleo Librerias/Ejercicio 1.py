import requests

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

def main():
    try:
        cantidad_bitcoins = float(input("Ingresa la cantidad de Bitcoins que posees: "))
        assert cantidad_bitcoins>0, ValueError('La cantidad de Bitcoins debe ser mayor a 0')
        precio_bitcoin = obtener_precio_bitcoin()

        if precio_bitcoin is not None:
            costo_en_usd = cantidad_bitcoins * precio_bitcoin
            print(f"El costo de {cantidad_bitcoins} Bitcoins es: ${costo_en_usd:,.4f}")

    except ValueError:
        print("Ingresa una cantidad válida de Bitcoins.")

if __name__ == "__main__":
    main()

