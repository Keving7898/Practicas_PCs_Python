import requests

def exchange_bitcoin():
    try:
        change_on = float(input("Ingrese numero de bitcoins en su cuenta de usuario: "))
    except ValueError:
        print("Dato invalido. Ingrese el numero según lo que se le pide")
        return

    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        exchange_USD = data["bpi"]["USD"]["rate_float"]
        amount = exchange_USD * change_on
        print(f'El monto equivalente es de $/{f"{amount:,.4f}"}')

    except requests.exceptions.RequestException as e:
        print("Se ha producido un error al obtener datos de la API", str(e))
    except KeyError:
        print("Se ha producido un error al analizar la respuesta de la API.")
    except (ValueError, TypeError):
        print("Se ha producido un error al realizar los cálculos")
    except Exception as e:
        print("Se ha producido un error inesperado:", str(e))

exchange_bitcoin()
