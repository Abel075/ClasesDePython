from modulos import saludo , mascotas                   # funcion muy importante para repartir codigo en diferentes sectores de la aplicacion
from camelcase import CamelCase


 #Instalando y probando el modulo CamelCase
 #pip install camelcase
 #desinstalando un modulo
 #pip uninstall camelcase

saludo('Abel')

c = CamelCase()
s = "esta oracion necesita CamelCase"

camelcase = c.hump(s)

print(camelcase)