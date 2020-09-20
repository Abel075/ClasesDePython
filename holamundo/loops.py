# # Loops de while / repeticiones

# i = 0 

# while i < 5: #condicion
#     i += 1
    
#     # i = i+1 #aumento de valor de i
#     if i == 3:
#         continue
#     print(i)


# For loop


# usuarios = ['Chanchito feliz', 'Felipe', 'Roberto', 'Nicolas']

# for usuario in usuarios:
#     print(usuario)

# usuario = 'Chanchito feliz'

# for c in usuario:
#     print(c)

# usuarios = ['Chanchito feliz', 'Felipe', 'Roberto', 'Nicolas']

# for usuario in usuarios:
#     if usuario == 'Roberto':
#         break
#     print(usuario)


# usuarios = ['Chanchito feliz', 'Felipe', 'Roberto', 'Nicolas']

# for usuario in usuarios:
#     if usuario == 'Roberto':
#         continue
    # print(usuario)

# for x in range(3,30, 3):
#     print(x)
# else:
#     print('Hemos terminado')

usuarios = ['Chanchito feliz', 'Felipe', 'Roberto', 'Nicolas']

edades = [24,25,26,35]

for usuario in usuarios:
    for edad in edades:
        print(usuario,edad)