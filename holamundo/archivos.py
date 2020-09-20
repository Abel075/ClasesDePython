# Leer archivos

# permisos:
# 'r' read = leer
# 'a' append = Agregar mas texto al final del archivo
# 'w' write = Crear archivo si no existe o abrir en caso que exista
# 'x'       = Crea un archivo si no existe, pero da error si existe

# read = lee todo el documento, cuidado con documentos pesados
# readline = lee linea por linea 


# c = open('chanchito.txt', 'w')

# c.write('\nagregamos una nueva linea a nuestro archivo') # agregado de nuevas lineas al documento

# c.close()   # Siempre es buena practica cerrar el archivo despues de leerlo/abrirlo

# x = open('chanchito.txt')

# print(x.read())

# eliminar archivos en el sistema operativo
import os
if os.path.exists('chanchitos.txt'):
    os.remove('chanchito.txt')
else:
    print('El archivo no existe')

os.rmdir('mkiCarpeta')  # borra directorios