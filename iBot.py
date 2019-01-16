from pyknow import *

from  hablarBot import *

global nombre2
#
# class nombreClase(object):
#
#     def __init__(self,nombre):
#
#         self.nombre = nombre
#
#         nombre2 = self.nombre
#
#     def setNombre(self,nombre):
#
#
#         self.nombre = nombre
#
#     def getNombre(self):
#
#         return self.nombre

def setNombre(nombre):

    global  nombre2

    nombre2 = nombre


class saludo(Fact):

    """Saludo bot"""

    pass

class tiempo(Fact):

    """tiempobot"""

    pass

class nombre(Fact):

    pass


class respuestasBot(KnowledgeEngine):

    @Rule(saludo(saludos='saludo2'))
    def saludo2(self):
        print("Hola :) ")
        hb = HablarBot()
        hb.hablarBot("hola\n")

    @Rule(saludo(saludos='saludo1'))
    def saludo1(self):
        print("Booonjoooooournooou")
        hb = HablarBot()
        hb.hablarBot("Booonjoooooournooou\n")

    @Rule(tiempo(tiempos='nublado'))
    def tiempo1(self):
        print("Esta muy nublado, acuerdate de llevar abrigo")
        hb = HablarBot()
        hb.hablarBot("Esta muy nublado, acuerdate de llevar abrigo\n")


    @Rule(tiempo(tiempos='soleado'))
    def tiempo2(self):
        print("Esta muy soleado, ¿llevas gorra?")
        hb = HablarBot()
        hb.hablarBot("Esta muy soleado, ¿llevas gorra?\n")

    @Rule(nombre(nombreResp="nombre1"))
    def nombre1(self):
        #print(nombre2)
        hb = HablarBot()
        print("\nEs un buen nombre " + nombre2 + "\n")
        hb.hablarBot("Es un buen nombre ",nombre2)

