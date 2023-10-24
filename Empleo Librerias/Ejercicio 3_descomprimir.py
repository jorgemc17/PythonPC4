import zipfile

archivo_zip = 'imagen.zip'
carpeta_salida = 'imagenes_descomprimidas'

import os
os.makedirs(carpeta_salida, exist_ok=True)

with zipfile.ZipFile(archivo_zip, 'r') as zipf:
    zipf.extractall(carpeta_salida)
