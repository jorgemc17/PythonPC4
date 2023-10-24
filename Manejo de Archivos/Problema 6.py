def contar_lineas_de_codigo(archivo):
    try:
        with open(archivo, 'r') as file:
            lineas = file.readlines()
            lineas_de_codigo = 0
            comentario_multilinea = False

            for linea in lineas:
                linea = linea.strip()  
                if not comentario_multilinea:
                    if not linea.startswith("#") and linea:
                        lineas_de_codigo += 1

                    if "'''" in linea or '"""' in linea:
                        comentario_multilinea = not comentario_multilinea
                elif "'''" in linea or '"""' in linea:
                    comentario_multilinea = not comentario_multilinea

            return lineas_de_codigo
    except FileNotFoundError:
        return None

archivo = input("Ingrese la ruta del archivo .py: ")

if archivo.endswith(".py"):
    lineas_de_codigo = contar_lineas_de_codigo(archivo)
    if lineas_de_codigo is not None:
        print(f"Líneas de código en {archivo}: {lineas_de_codigo}")
    else:
        print("El archivo no fue encontrado.")
else:
    print("El archivo no tiene una extensión .py válida.")
