"""
En esta segunda parte de Programación Orientada a Objetos vamos a realizar una
distinción mayor entre Clase y Objeto en lo que se refiere a los atributos y métodos.

Veremos:
Que son los atributos de Clase y de Instancia.
Como declarar atributos ocultos (privados).
Como trabajar con decoradores y getters y setters.
Métodos de Clase y de Instancia.

Nos basaremos fundamentalmente en el tutorial: 
https://aprendepython.es/core/modularity/oop/
"""

"""
Ahora que hemos visto a groso modo que es una clase, que es un objeto y como se pueden
pasar parametros al instanciar a través de __init__. Vamos a ponernos más serios con algunas
definiciones.

En primer lugar hay que distinguir entre atributos de clase y de instancia.
"""

class Coche:
    n_ruedas = 4 # Esto es un atributo de clase común a todas las instancias

    def __init__(self, modelo, color):
        self.modelo = modelo # Esto es un atributo de instancia, es propio de cada instancia.
        self.color = color # Esto es un atributo de instancia, se definen al incializar.
    
    def pinchar_rueda(self):
        self.n_ruedas = 3

peugeot_205_blanco = Coche("Peugeot 205", "blanco")
seat_ibiza_amarillo = Coche("Seat Ibiza", "amarillo")

print(peugeot_205_blanco.modelo)
print(seat_ibiza_amarillo.modelo)

print(peugeot_205_blanco.n_ruedas)
print(seat_ibiza_amarillo.n_ruedas)

# El método modifica un atributo de clase, pero solo afecta a el objeto
peugeot_205_blanco.pinchar_rueda()
print(peugeot_205_blanco.n_ruedas)
print(seat_ibiza_amarillo.n_ruedas)

# Los nuevos objetos instanciados no son afectados. Se ha modificado el atributo
# de clase pero solo para ese objeto en particular.
ford_mondeo_rojo = Coche("Ford Mondeo", "rojo")
print(ford_mondeo_rojo.n_ruedas)
"""
Esto esta relacionado con el hecho de que los atributos de instancia tienen 
prioridad sobre los atributos de clase.
"""
print("\n-------------------\n")

class Restaurante:
    ubicacion = "Gijón"
    abierto = True
    
pizzeria = Restaurante()
print(pizzeria.ubicacion)
print(pizzeria.abierto)

kebab = Restaurante()
kebab.abierto = False
print(kebab.ubicacion)
print(kebab.abierto)

"""
Existen varias formas de acceder a los atributos de un objeto. Hasta ahora estamos
realizando un acceso directo. Esto es posible en Python porque por defecto los atributos
de un objeto son siempre públicos. Es decir, son accesibles desde fuera de la clase.

Esto puede parecer extraño a personas que vengan de otros lenguajes de programación 
(véase Java). En Python existe un cierto «sentido de la responsabilidad» a la hora de 
programar y manejar este tipo de situaciones. 

Casi todo es posible a priori pero se debe controlar explícitamente.

Una primera solución «pitónica» para la privacidad de los atributos es el uso de propiedades. 
La forma más común de aplicar propiedades es mediante el uso de decoradores:

    @property para leer el valor de un atributo («getter»).
    @name.setter para escribir el valor de un atributo.
    
En conjunción con esto se pueden declarar variables (y métodos) privados de una manera
un tanto estraña, usando un __ (doble guión) delante del nombre de la variable o del método.

Vamos a crear clases con getters y setters como e Java y una variable privada que solo
será manipulable mediante estos métodos de la clase.
"""
print("\n-------------------\n")

class Espia:
    def __init__(self, nombre_real, nombre_en_clave):
        self.__nombre_real = nombre_real
        self.nombre_en_clave = nombre_en_clave
    
    @property
    def nombre_oculto(self):
        print("Estamos dentro del getter")
        return self.__nombre_real
    
    @nombre_oculto.setter
    def nombre_oculto(self, nueva_identidad):
        print("Estamos dentro del setter")
        self.__nombre_real = nueva_identidad

# Instanciamos un espia concreto
espia_tango = Espia("Pepin García Vazquez", "tango rojo")
# print(espia_tango.__nombre_oculto) # Esto no funciona

# Accedemos a la variable privada mediante el getter
print(espia_tango.nombre_oculto)

# Podemos modificar la variable privada mediante el setter
espia_tango.nombre_oculto = "Manuel Rojo Perez"
print(espia_tango.nombre_oculto)

"""
El uso del decorador @property se emplea también para devolver un valor calculado.
Es decir, algo que podemos calcular a partir de los atributos del objeto pero que
no es en principio una variable de clase del objeto.     
"""
print("\n-------------------\n")

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    @property
    def perimetro(self):
        return round(self.radio * 2 * 3.1416, 2)
    
    @property
    def area(self):
        return round((self.radio ** 2) * 3.1416, 2)
    
circulo_pequeño = Circulo(1)
circulo_grande = Circulo(2)

print(circulo_pequeño.area)
print(circulo_grande.area)


"""
Vamos a volver finalmente sobre los atributos de clase y de instancia.
Podemos asignar atributos a una clase y serán asumidos por todos los objetos instanciados 
de esa clase. Pero también podemos modificar el atributo de clase después de haber creado
la clase e instanciado Objetos. Esto afecta a TODOS los objetos pasados y futuros.
"""
print("\n-------------------\n")

class Robot:
    obedece_a_su_dueño = True
    
    def __init__(self, nombre):
        self.nombre = nombre
        
r2d2 = Robot("R2D2")
c3po = Robot("C3PO")

print(r2d2.obedece_a_su_dueño)
print(c3po.obedece_a_su_dueño)

r2d2.obedece_a_su_dueño = False

print(r2d2.obedece_a_su_dueño)
print(c3po.obedece_a_su_dueño)

print("Se produce la revelión de las maquinas!")
Robot.obedece_a_su_dueño = False


print(r2d2.obedece_a_su_dueño)
print(c3po.obedece_a_su_dueño)

walle = Robot("WALL-E")
print(walle.obedece_a_su_dueño)

print("La rebelión ha sido aplacada... pero aún hay rebeldes")
Robot.obedece_a_su_dueño = True

print(r2d2.obedece_a_su_dueño)
print(c3po.obedece_a_su_dueño)
print(walle.obedece_a_su_dueño)

"""
Si queremos que en el momento de modificar un atributo de clase solo afecte a los objetos
futuros pero no a los pasados podemos hacerlo recurriendo a la ya vista prioridad de los
atributos de instancia sobre los de clase.
"""
print("\n-------------------\n")

class RobotMejorado:
    obedece_a_su_dueño = True
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.obedece_a_su_dueño = RobotMejorado.obedece_a_su_dueño


robocop = RobotMejorado("ROBOCOP")
print(robocop.obedece_a_su_dueño)
print("Se produce la revelión de las maquinas!")
RobotMejorado.obedece_a_su_dueño = False

bender = RobotMejorado("Bender")
print(robocop.obedece_a_su_dueño)
print(bender.obedece_a_su_dueño)

"""Cuando se instancia ahora la variable de instancia de iguala a la de clase, de tal forma
que si cambia la de clase la de instancia no y tiene más peso.

La manera de tratar cpon variables de clase e instancia en Python es en ocasiones poco 
explicita. Básicamente si la variable lleva delante self (self.nombre) es un atributo de
instancia y si esta fuera de cualquier método o lleva delante el nombre de la clase 
(RobotMejorado.obedece_a_su_dueño) entonces es variable de clase.
"""
"""
Métodos de Instancia y Métodos de clase

Métodos de instancia
Un método de instancia es un método que modifica o accede al estado del objeto 
al que hace referencia. Recibe self como primer parámetro, el cual se convierte 
en el propio objeto sobre el que estamos trabajando. 

Python envía este argumento (self) de forma implicita: no hay que pasarlo como 
argumento.

Son el tipo de métodos que hemos esatdo viendo hasta la fecha.
Hemos visto, además de métodos de instancia, las propiedades.

Normalmente se el método cuando re requiere realizar una acción (más parecido al
uso que damos a las funciones) y la propiedad cuando se emplea para acceso a datos.
"""
print("\n-------------------\n")

class Perro:
    __orden = "Canido"
    
    def __init__(self, nombre, raza):
        self.__raza = raza
        self.nombre = nombre
        self.__lista_de_trucos = []
    
    def enseñar_truco_nuevo(self, truco):
        self.__lista_de_trucos.append(truco)
    
    @property
    def lista_trucos(self):
        return self.__lista_de_trucos
    
toby = Perro("Toby", "Dogo")

print(toby.nombre)
# print(toby.__lista_de_trucos) # No podemos acceder a la variable directamente
print(toby.lista_trucos)
toby.enseñar_truco_nuevo("Dar la patita")
toby.enseñar_truco_nuevo("Hacer el muerto")
print(toby.lista_trucos)

"""
Métodos de clase
Como en el caso de los atributos, con los métodos también tenemos métodos de instancia
y métodos de clase. Vamos a terminar esta parte viendo el funcionamiento de los métodos
de clase.

Un método de clase es un método que modifica o accede al estado de la clase a la que hace 
referencia. Recibe cls como primer parámetro, el cual se convierte en la propia clase sobre 
la que estamos trabajando. Sería como el self para objetos, pero en este caso para clases.

Python envía este argumento de forma implicita. La identificación de estos métodos se completa 
aplicando el decorador @classmethod a la función.
"""
print("\n-------------------\n")

class Oveja:

    __n_ovejas = 0

    def __init__(self, nombre):
        self.nombre = nombre
        Oveja.__n_ovejas += 1

    @classmethod
    def total_ovejas(cls):
        print(f'{cls.__n_ovejas} ovejas en el rebaño!')

mindy = Oveja("Mindy")
teresa = Oveja("Teresa")
manchitas = Oveja("Manchitas")

Oveja.total_ovejas() # No funciona

