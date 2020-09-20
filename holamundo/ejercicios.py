# dato = input('Ingrese dato: ')

# lista = ['hola', 'mundo', 'chanchito', 'feliz', 'dragones']  

# if lista.count(dato) > 0 :                      # verificar si existe un dato en la lista   
#     print('El dato existe:', dato)
# else:
#     print('El dato no exite :(', dato)


primero = input('Ingrese primer numero: ')

try:                                                  # Intenta cambiar un string a un entero
    primero = int(primero)
except:
    primero = 'chanchito feliz'



if primero == 'chanchito feliz':
    print('El valor ingresado no es un entero')
    exit()

segundo = input('Ingrese el segundo numero: ')

try:                                                  # Intenta cambiar un string a un entero
    segundo = int(segundo) 
except:
    segundo = 'chanchito feliz'

if segundo == 'chanchito feliz':
    print('El valor ingresado no es un entero')
    exit()


# calculadora
simbolo = input('Ingrese la operacion: ')

if simbolo == '+':
    print('Suma:' , primero + segundo)

elif simbolo == '-':
    print('Resta:' , primero - segundo)

elif simbolo == '*':
    print('Multiplicacion' , primero * segundo)

elif simbolo == '/':
    print('Division:' , primero / segundo)

else:
    print('El simbolo ingresado no es valido')    

