from pyfiglet import Figlet
import random

figlet = Figlet()

fuentes_disponibles = figlet.getFonts()

fuente_seleccionada = input("Ingresa la fuente o presiona Enter (al azar):\n")
if not fuente_seleccionada:
    fuente_seleccionada = random.choice(fuentes_disponibles)

figlet.setFont(font=fuente_seleccionada)

texto_imprimir = input("Ingresa el texto que deseas imprimir:\n")

print(figlet.renderText(texto_imprimir))

