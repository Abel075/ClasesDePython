
#Multiplicar dos numeros sin usar el simbolo multiplicacion

a = 4
b = 8

resultado = 0

for x in range(a):
    resultado += b

print(resultado)

#Ingresar nombre y apellido e imprimirlo al reves

nombre = 'Abel'
apellido = 'Correa'

concatenacion = nombre + ' ' + apellido

print(concatenacion[::-1])

#Escribir una funcion que encuentre el elemento menor de una lista

lista = [1,2,3,4,55,-24,-13]

menor = "init"

for x in lista:
    if menor == 'init':
        menor = x
    else:
        menor = x if x < menor else menor  # evaluacion: quiero que menor sea x siempre y cuando x sea menor que la variable de menor, sino no cambia

print('menor', menor)

#Escribir una funcion que devuelva el volumen de una esfera por su radio

def calcularVolumen(r):
    return 4/3 * 3.14 * r**3 

resultado = calcularVolumen(6)
print(round(resultado,3))

#Escribir una funcion que indique si el usuario es mayor de edad

def esMayor(usuario):
    return usuario.edad >17

class Usuario:
    def __init__(self,edad):
        self.edad = edad

usuario = Usuario(15)
usuario2 = Usuario(21)

resultado1 = esMayor(usuario)
resultado2 = esMayor(usuario2)

print(resultado1, resultado2)

#Escribir una funcion que indique si una funcion es par o impar

def esPar(n):
    return n % 2 == 0

resultado = esPar(11)

print(resultado)

# Escribir una funcion qeu indique cuantas voocales tiene una palabra

palabra = 'ChAnchitoFeliz'

vocales = 0
for x in palabra:
    y = x.lower()
    vocales += 1 if y == 'a' or y == 'e' or y == 'i' or y == 'o' or y == 'u' else 0

print(vocales)


#Escribir una aplicacion que reciba una cantidad infinita de numeros hasta decir basta
#luego qeu devuelva la suma de los numeros ingresados

# lista = []
# print('Ingrese numeros y para salir escriba basta')
# while True:
#     valor = input('Ingrese valor: ') 
#     if valor == 'basta':
#         break
#     else:
#         try:
#             valor = int(valor)
#             lista.append(valor)
#         except:
#             print('Dato invalido')
#             exit()

# resultado = 0

# for x in lista:
#     resultado += x

# print(resultado)

#Escribir una funcion que reciba nombre y apellido y los vaya agregando a un archivo

def agregaNombreAArchivo(nombre, apellido):
    c = open('nombrecompleto.txt', 'a')
    c.write(nombre + ' ' + apellido + '\n')
    c.close()

agregaNombreAArchivo('Abel', 'Correa')