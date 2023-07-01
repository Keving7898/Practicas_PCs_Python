import requests
import csv

def bitcoin_values(data_json):
    try:
        data = data_json.json()

        valores_monedas = {}
        for monedas, detalles in data['bpi'].items():
            valores_monedas[monedas] = detalles['rate_float']

        with open('Valor_cambio.txt', 'w') as f:
            for monedas, valor in valores_monedas.items():
                f.write(f'{monedas}: {valor}\n')

        csv_headers = ['Moneda', 'valor']
        csv_rows = [[monedas, valor] for monedas, valor in valores_monedas.items()]

        with open('Valor.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(csv_headers)
            writer.writerows(csv_rows)

        print("Datos guardados exitosamente.")

    except IOError as e:
        print("Ocurrio un error al guardar el archivo:", str(e))
    except Exception as e:
        print("Ocurrio un error inesperado:", str(e))



url='https://api.coindesk.com/v1/bpi/currentprice.json'
dat_response=requests.get(url)

bitcoin_values(dat_response)

