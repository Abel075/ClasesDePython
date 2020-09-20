
# Clases = planos de lo que queremos crear
# Objetos = instancias de estos planos, por ejemplo la casa ya contruida




# class Usuario:
#   def __init__(self, nombre, apellido):  # __init__ se ejecuta siempre cuando creamos una instancia de estas clases.
#     self.nombre = nombre                 # Self hace referencia a una istancia que nosostros creamos, pudiendo cambiar los valores de las propiedades de estas instancias
#     self.apellido = apellido

#   def saludo(self):
#       print('Hola!, mi nombre es', self.nombre, self.apellido)  # Metodo saludo




# class Admin(Usuario):
#     def superSaludo(self):
#         print('Hola me llamo', self.nombre, 'y soy administrador')


# usuario = Usuario('Felipe', 'Feliz') # si debemos pasar los parametros para la creacion  de esas instancias
# # usuario2 = Usuario('Chanchito', 'Feliz')

# usuario.saludo()
# usuario.nombre = 'Chanchito'
# # usuario.saludo()
# # del usuario

# admin = Admin('Super', 'Feliz')
# admin.saludo()
# admin.superSaludo()

class Animal:
    def __init__(self, nombre, onomatopeya):            # Propiedades
        self.nombre = nombre
        self.onomatopeya = onomatopeya

    def saludo(self):
        print('Hola soy un', self.tipo,  'y mi sonido es: ', self.onomatopeya)  #MEtodo
    
   


class Gato(Animal):                                     # Objeto Gato, hijo de Animal
    tipo = 'gato'

    def __init__(self,nombre,onomatopeya):
        Animal.__init__(self, nombre, onomatopeya)      # Primera forma de extender del padre
        print('Hola soy un gato extendido')

class Perro(Animal):                                     # Objeto Perro, hijo de Animal
    tipo = 'perro'

    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre,onomatopeya)              # segunda forma de exteder del padre
        print('Instanciando un perro')

class Canario(Animal):
    tipo = 'canario'
    
gato = Gato('Floffy', 'maullido')
gato.saludo()

perro = Perro('Firulais', 'ladrido')
perro.saludo()

canario = Canario('Piolin', 'silvido')
canario.saludo()

