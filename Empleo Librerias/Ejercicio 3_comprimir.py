import zipfile

imagen_filename = '/workspaces/PythonPC4/img/mi_imagen.jpg'
archivo_zip = 'imagen.zip'

with zipfile.ZipFile(archivo_zip, 'w') as zipf:
    zipf.write(imagen_filename, arcname='imagen.jpg')
