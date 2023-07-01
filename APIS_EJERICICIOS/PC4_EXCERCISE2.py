import pyfiglet
import random

def impreso_fuente():
    try:

        fuentes_disponibles = pyfiglet.FigletFont.getFonts()

        fuente_selecionada = input("Ingrese el nombre de la fuente (si lo deja, se escogerá uno al azar): ")

        if not fuente_selecionada:
            fuente_selecionada = random.choice(fuentes_disponibles)

        figlet = pyfiglet.Figlet(font=fuente_selecionada)

        texto_fuente = input("Escriba un texto: ")

        print(figlet.renderText(texto_fuente))

    except pyfiglet.FigletError as e:
        print("Error:Fuente invalida.")
        
    except Exception as e:
        print("Un error inesperado ha ocurrido:", str(e))


impreso_fuente()
