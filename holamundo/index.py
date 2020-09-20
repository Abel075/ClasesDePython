
# Aca va un  comentario de python

# 

if 3>5 :
    print('Esto no se va a imprimir')

# if 5>3 :
#     print('5 es mayor que 3')    
    
x = 5
y = 'chanchito feliz'

print(x,y)  

email = 'canchito@feliz.com'

print(email)

mivar = 'canchito'
MIVAR = 'chanchito' # mayusculas en la variable se usan para constantes

a,b,c = "Lala", 'Lele', 'Lili'

print('a,b,c')

valor1 = valor2 =valor3 = 'chanchito feliz'

print(valor1,valor2,valor3)

inicio = 'Hola '
final = 'mundo'

print(inicio + final)

# tipos de datos

palabra = 'hola mundo' #string
oracion = "hola mundo comilla doble" #string

entero = 20 #integer
conDecimales = 20.2 #float
complejos = 1j

print(palabra, oracion,entero,conDecimales,complejos)


#listas

listas = ['Hola', 'mundo', 'Chanchito feliz'] #lista vacia
listas2 =listas.copy()
listas.append('Chanchito triste') # append agrega datos a la lista
# listas.clear() #.clear() limpia la lista

# print(listas,listas2.count(3))
# print(len(listas), len(listas2))

largoLista = len(listas)
largoListas2= len(listas2)

# print(largoLista,largoListas2)

# print(listas[2]) #simpre pensar en el indice, no en la ubicacion real del elemnto

# listas.pop() #remueve el ultimo elemento de la lista
# listas.remove('Hola') #Este elimina un elemto por su valor
listas.reverse()
listas.sort()
tupla = ('hola', 'mundo', 'somos', 'tupla') # las tuplas no son modificables por ejemplo con .append / solo se puede trsnformandola en lista
listaDeTupla = list(tupla) # transformar una tupla a lista
listaDeTupla.append('Chanchito') 

print(listaDeTupla)

rango = range(6) #funcion rango
print(rango)

# Diccionarios

diccionario = {                         #Declaracion de datos del diccionario, con llaves

    "nombre" : "Chanchito feliz",
    "raza" : "Persa",
    "edad" : 5
}

# print(diccionario)
# print(diccionario['nombre'])    # Busqueda de valores dentro del diccionario
print(diccionario.get('nombre'))  #otra forma de buscar valores en le diccionario


diccionario['nombre'] = 'Fluffy'  # cambiar valores en el diccionario

print(len(diccionario))    #metodo len cantidad de valores en el diccionario

diccionario['ronronea'] = 'si' # agregar valores en el diccionario
print(diccionario)
# diccionario.pop('ronronea')  # Eliminar un valor en el diccionario
# diccionario.popitem()   # Elimina el ultimo valor del diccionario
# copiaGatito = diccionario.copy() # copiar
copiaGatito = dict(diccionario)
del diccionario['ronronea'] # Igual que la funcion pop elimina un valor en diccionario
diccionario.clear()
print(diccionario, copiaGatito)


fluffy = {

    'nombre': "Fluffy",
    'edad': 4
        
} 

mamba = {
    'nombre': "Black Mamba",             # Diccionarios anidados
    'edad': 12
    
}
gatitos = {

     "Fluffy" : fluffy,  
     "Mamba"  : mamba
    
}

print(gatitos)

# Constructor Dict

perritos = dict(nombre="Chanchito feliz", edad=6)   # Forma dict de crear diccionarios
print(perritos)



# Booleanos true or false  \   util para control de flujo

verdadero = True
falso = False

print(verdadero, falso)


#  control de flujo









