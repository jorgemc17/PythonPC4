""" Escriba un programa que realice las siguientes tareas 
(Puede usar clases y/o funciones,
también puede usar un menú para organizar su programa):
- Solicite un número entero entre 1 y 10 y guarde en un fichero con el nombre
tabla-n.txt la tabla de multiplicar de ese número, donde n es el número 
introducido.
- Solicite un número entero entre 1 y 10, lea el fichero tabla-n.txt con la tabla 
de multiplicar de ese número, donde “n” es el número introducido, y la muestre por
pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando
de ello.
- Solicite dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la 
tabla de multiplicar de ese número, y muestre por pantalla la línea m del 
fichero. Si el fichero no existe debe mostrar un mensaje por pantalla 
informando de ello.

Notas:
- Note que dentro del manejo de errores existe una excepción de tipo
FileNotFoundError la cual le será de mucha utilidad.
- Revise los métodos de cadena
- Dentro del open() el método “readlines” le podría ser de utilidad. """

def guardar_tabla_multiplicar(numero):
    with open(f'tabla-{numero}.txt', 'w') as archivo:
        for i in range(1, 11):
            resultado = numero * i
            archivo.write(f'{numero} x {i} = {resultado}\n')
    print(f'Tabla de multiplicar del {numero} guardada en tabla-{numero}.txt')


def mostrar_tabla_multiplicar(numero):
    try:
        with open(f'tabla-{numero}.txt', 'r') as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print(f'El archivo tabla-{numero}.txt no existe.')


def mostrar_linea_tabla(numero, linea):
    try:
        with open(f'tabla-{numero}.txt', 'r') as archivo:
            lineas = archivo.readlines()
            if 1 <= linea <= 10:
                print(lineas[linea - 1])
            else:
                print(f'Línea {linea} fuera de rango. Debe estar entre 1 y 10.')
    except FileNotFoundError:
        print(f'El archivo tabla-{numero}.txt no existe.')

while True:
    print('1. Guardar tabla de multiplicar')
    print('2. Mostrar tabla de multiplicar')
    print('3. Mostrar línea de la tabla')
    print('4. Salir')

    opcion = input('Seleccione una opción: ')

    if opcion == '1':
        numero = int(input('Introduce un número entre 1 y 10: '))
        if 1 <= numero <= 10:
            guardar_tabla_multiplicar(numero)
        else:
            print('Número fuera de rango. Debe estar entre 1 y 10.')
    elif opcion == '2':
        numero = int(input('Introduce un número entre 1 y 10: '))
        mostrar_tabla_multiplicar(numero)
    elif opcion == '3':
        numero = int(input('Introduce un número entre 1 y 10: '))
        linea = int(input('Introduce el número de línea (1-10): '))
        mostrar_linea_tabla(numero, linea)
    elif opcion == '4':
        break
    else:
        print('Opción no válida. Por favor, seleccione una opción válida.')
