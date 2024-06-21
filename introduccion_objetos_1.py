"""
Vamos a tratar aqui una pequeña introdución a la Programación
Orientada a Objetos en Python. Trataremos sobre clases, objetos, 
atributos y métodos.

Como en otras ocasiones nos basamos en el titorial oficial de Python3.8
en español: https://docs.python.org/es/3.8/tutorial/index.html

También en: https://aprendepython.es/core/modularity/oop/
"""


"""
Programación Orientada a Objetos (POO)
Para entender este paradigma primero tenemos que comprender qué es una clase
y qué es un objeto. Un objeto es una entidad que agrupa un estado y una 
funcionalidad relacionadas. 

El estado del objeto se define a través de variables llamadas atributos, 
mientras que la funcionalidad se modela a través de funciones a las que 
se les conoce con el nombre de métodos del objeto.

Una clase, por otro lado, no es más que una plantilla genérica a partir
de la cuál instanciar los objetos; plantilla que es la que define qué 
atributos y métodos tendrán los objetos de esa clase.

En Python las clases se definen mediante la palabra clave class seguida del 
nombre de la clase, dos puntos (:) y a continuación, indentado, el cuerpo de 
la clase. Como en el caso de las funciones, si la primera línea del cuerpo se 
trata de una cadena de texto, esta será la cadena de documentación de la clase 
o docstring.
"""
# Declaración de una clase vacía con Docstring
class ClaseVacia:
    """Esta es una clase vacia sin atributos ni métodos.
    """
    pass

"""
Primer vistazo a las clases:
Los objetos clase soportan dos tipos de operaciones: hacer referencia a atributos 
e instanciación. Veremos a que nos referimos con esto, pero primero creemos una
clase no vacía con un método y un atributo.
"""
# Creamos una clase sencilla
class Bicicleta:
    """Un ejemplo de clase Bicicleta.
    """
    def __init__(self, dueño, color, radio=2):
        self.color = color
        self.dueño = dueño
        self.perimetro = radio * 2 * 3.1416
    
    def frenar(self):
        print("La bicleta frena")

    def subir_piñon(self, n_piñones):
        print(f"Subimos {n_piñones} piñones")
        return n_piñones

    def bajar_piñon(self):
        print("Bajar piñon")

# Vamos a INSTANCIAR la clase y de esta manera crear un objeto asignado a una variable
bicleta_dani = Bicicleta("Dani", "amarillo")
bicleta_vicente = Bicicleta("Vicente", "rojo")

# Usar métodos de la bicicleta
bicleta_dani.bajar_piñon()
bicleta_dani.subir_piñon(2)
bicleta_dani.frenar()

# Acceso a los atributos
print(bicleta_dani.dueño)
print(bicleta_dani.color)

print(bicleta_vicente.dueño)
print(bicleta_vicente.color)

bicleta_dani.color = "blanco"

print(bicleta_dani.dueño)
print(bicleta_dani.color)

"""
La instanciación de clases usa la notación de funciones. Date cuenta de 
que el objeto de clase es una función sin parámetros que retorna una nueva
instancia de la clase, es decir, un objeto.

Podemos verlo como que la clase es la IDEA del Objeto y el Objeto es el objeto
real, una manifestación una instancia usable de esa clase.

A partir de una clase podemos crear tantos objetos como queramos mediante instancias.
"""

"""
Muchas clases necesitan crear objetos con instancias en un estado inicial particular. Por
lo tanto sería util poder epecificar ciertos atributos en al instancia un objeto concreto.

Una clase puede definir un método especial llamado __init__(). El método __init__ se ejecuta 
justo después de crear un nuevo objeto a partir de la clase, al instanciar. El método __init__ 
sirve, como sugiere su nombre, para realizar cualquier proceso de inicialización que sea necesario.
Comúnmente en programación a un método de clase como este se le llama Constructor.

Notar que ya en varias ocasiones a aparecido la palabra self. Esta sentencia de python indica en
el contexto de las clases una referencia a la propia clase. Al pasarlo a una función como primer
argumento indicamos que es una función de la clase, es decir, un método.
"""
class Persona:
    def __init__(self, nombre, apellidos, altura, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.altura = altura
        self.edad = edad

# Creamos un Objeto, instanciamos una persona concreta con su estado, sus atributos
pepin = Persona("Pepin", "García Vazquez", 1.8, 45)
print(pepin.nombre)

# Podemos ahora instanciar las personas concretas que sean necesarias
paloma = Persona("Paloma", "Fernandez Izquierdo", 1.65, 30)
print(paloma.nombre)

# Estos atributos son accesibles y modificables        
paloma.edad = 31
print(paloma.edad)

# Incluso podriamos crear a posteriori atributos nuevos
# Python nos permite añadir atributos dinámicamente a un objeto 
# incluso después de su creación
paloma.color_pelo = "negro"
print(paloma.color_pelo)

"""
Además de todo esto los atributos de una clase también pueden ser definidos desde dentro de
un método. De esta froma el atributo no existe hasta llamar al método o el método puede
modificar el atributo.
"""
del paloma
del pepin
del bicleta_dani, bicleta_vicente
 
print("\n------------------------")

class Guitarra:
    def __init__(self, tipo, marca):
        self.n_cuerdas = 6
        self.tipo = tipo
        self.marca = marca
    
    def afinar(self, nota):
        self.afinacion = nota
        print("Pliiiiiimm, pluummmm...")
    
    def tocar(self):
        print("Suena una hermosa melodia...")
        
    def romper_cuerda(self):
        self.n_cuerdas -= 1
        print("Plack!! Una cuerda menos...")

guitarra_electrica = Guitarra("electrica", "gibson")

guitarra_electrica.afinar("Mi")
print(guitarra_electrica.afinacion)
guitarra_electrica.tocar()
guitarra_electrica.romper_cuerda()
print(guitarra_electrica.n_cuerdas)

# Primera tanda de ejercicios

