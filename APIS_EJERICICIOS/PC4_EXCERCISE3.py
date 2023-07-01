#PROBLEMA 3
import requests

def puppies_download(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        with open('perrito_2.jpg', 'wb') as f:
            f.write(response.content)

        print("Descarga exitosa.")

    except requests.exceptions.RequestException as e:
        print("Ocurrio un error al obtener la imagen:", str(e))

    except IOError:
        print("Ocurrio un error mientras se guardaba la imagen.")

    except Exception as e:
        print("Error inesperado:", str(e))

url_1 = 'https://plus.unsplash.com/premium_photo-1668918112539-9299ea40ac20?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wxMjA3fDB8MXxzZWFyY2h8MzB8fHBlcnJpdG98ZXN8MHx8fHwxNjg4MDQ0MjgwfDE&ixlib=rb-4.0.3&q=80&w=1080'

puppies_download(url_1)
