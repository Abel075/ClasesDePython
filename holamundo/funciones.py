

#funciones
# Pueden recibir argumentos: que son varibles que no sotros podemos usar dentro de nuestras funciones para que sean flexibles dependiendo de la necesidad que tengamos.

def miFuncion():
    print('Mi primera funcion!')


# miFuncion()    


# def imprimeDatos(nombre, apellido):
#     print('El nombre completo es', nombre, apellido) # argumentos son internas de la funcion
    
# imprimeDatos('Chanchito')  #Parametros para llamar los argumentos de la funcion, si la funcion tiene dos argumentos hay que pasarle dos parametros

# Metodo flexible

# def imprimeDatos(*nombre): # * para datos varibles, como si fuera una lista
#     print('El nombre completo es', nombre[1])
    
# imprimeDatos('Chanchito', 'Feliz', 'lala', 'lele')  #Parametros para llamar los argumentos de la funcion, si la funcion tiene dos argumentos hay que pasarle dos parametros

# def nombreCompleto(apellido, nombre):
#     print(nombre,apellido)

# # nombreCompleto(nombre='Chanchito',apellido='Feliz')


# def nombreCompleto2(**kwargs):
#     print(kwargs['nombre'],kwargs['apellido'])

# nombreCompleto2(nombre="Chanchito", apellido="Feliz")

def miFuncion2(argumento = 'Chanchito'):
    print(argumento)

miFuncion2('Batman')
miFuncion2() 

# def miFuncionLista(lista):
#     for el in lista:
#         print(el)

# miFuncionLista(['Chanchito','Feliz'])

def concatenaNombres(lista):
    i = ''
    for el in lista:
        i= i + el + ''
    return i

# nombres = concatenaNombres(['Chanchito', 'Feliz'])    
# print(nombres)


# Recursividad


def recursion(i):
    if (i < 1):
        return i
    print(i)
    recursion(i - 1)
recursion(6)