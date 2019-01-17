from pyknow import *

from  hablarBot import *



global nombreUsuario
global edadUsuario
global estudUsuario
global origenUsuario

global hb

hb = HablarBot()

nombreUsuario = "Amig@"
edadUsuario = 00
estudUsuario = "nada"
origenUsuario= "nada"

def gaspar():

    print("------------------------")
    print("Gaspar Habla: ")

def setNombre(nombre):

    global  nombreUsuario

    nombreUsuario = nombre

def setEdad(edad):

    global edadUsuario
    edadUsuario = edad

def setEstudio(estudia):

    global estudUsuario
    estudUsuario = estudia

def setOrigen(origen):

    global origenUsuario
    origenUsuario = origen


class saludo(Fact):

    """Saludo bot"""

    pass

class tiempo(Fact):

    """tiempobot"""

    pass

class nombre(Fact):

    pass

class edad(Fact):
    pass
class estudio(Fact):
    pass
class defectoPor(Fact):
    pass
class origen(Fact):
    pass


class respuestasBot(KnowledgeEngine):



    @Rule(saludo(saludos='saludo2'))
    def saludo2(self):

        gaspar()
        print("Hola :) ")
        hb.hablarBot("hola\n")

    @Rule(saludo(saludos='saludo1'))
    def saludo1(self):
        gaspar()
        print("Booonjoooooournooou")
        hb.hablarBot("Booonjoooooournooou\n")

    @Rule(tiempo(tiempos='nublado'))
    def tiempo1(self):

        gaspar()
        print("Esta muy nublado, acuerdate de llevar abrigo")
        hb.hablarBot("Esta muy nublado, acuerdate de llevar abrigo\n")


    @Rule(tiempo(tiempos='soleado'))
    def tiempo2(self):
        gaspar()
        print("Esta muy soleado, ¿llevas gorra?")
        hb.hablarBot("Esta muy soleado, ¿llevas gorra?\n")


    @Rule(nombre(nombreResp="nombre1"))
    def nombre1(self):
        gaspar()
        print("Es un buen nombre " + nombreUsuario)
        hb.hablarBot("Es un buen nombre " + str(nombreUsuario))
        gaspar()
        print("¿Que edad tienes " + nombreUsuario + "?")
        hb.hablarBot("Que edad tienes " + str(nombreUsuario) + "?")

    @Rule(edad(edadResp="edad1"))
    def edad1(self):
        if edadUsuario >= 18:
            gaspar()
            print("Vaya vaya eres todo un adulto")
            hb.hablarBot("Vaya vaya eres todo un adulto")
            gaspar()
            print("¿Que estudias " + str(nombreUsuario) + "?")
            hb.hablarBot("¿Que estudias " + str(nombreUsuario) + "?")
        if edadUsuario < 18:
            gaspar()
            print("Menor de edad!")
            hb.hablarBot("Menor de edad!")

    @Rule(defectoPor(defectoResp="pordefecto"))
    def defectopor1(self):

        gaspar()
        print("no entiendo lo que me intentas decir")
        hb.hablarBot("no entiendo lo que me intentas decir")

    @Rule(defectoPor(defectoResp="1"))
    def defectopor1(self):
        gaspar()
        print("no entiendo lo que me intentas decir.")
        hb.hablarBot("no entiendo lo que me intentas decir")

    @Rule(defectoPor(defectoResp="2"))
    def defectopor2(self):
        gaspar()
        print("Puedes repetirme, fuiste muy rapido.")
        hb.hablarBot("Puedes repetirme, fuiste muy rapido")

    @Rule(defectoPor(defectoResp="3"))
    def defectopor1(self):
        gaspar()
        print("lo siento, no estaba prestando atención.")
        hb.hablarBot("lo siento, no estaba prestando atención")

    @Rule(origen(origenResp='origen1'))
    def origen1(self):

        if (edadUsuario < 19 and origenUsuario == "Antofagasta" or origenUsuario == "antofagasta"):
            gaspar()
            print(origenUsuario + ", la perla del norte, " + nombreUsuario + " me recomendarias un buen lugar?")
            hb.hablarBot(origenUsuario + ", la perla del norte, " + nombreUsuario + " me recomendarias un buen lugar?")

        if (edadUsuario > 19 and origenUsuario == "Antofagasta" or origenUsuario == "antofagasta"):
            gaspar()
            print(origenUsuario + ", la perla del norte, " + nombreUsuario + " debes conocer de una buena playa, ¿me recomendarias una?")
            hb.hablarBot(origenUsuario + ", la perla del norte, " + nombreUsuario + " debes conocer de una buena playa, ¿me recomendarias una?")

        if (origenUsuario == "Iquique" or origenUsuario == "iquique"):
            gaspar()
            print("Asi que eres de " + origenUsuario + ", Tierra de campeones!, tienes " + str(edadUsuario) + "años, debiste haber vivido un fuerte terremoto")
            hb.hablarBot("Asi que eres de " + origenUsuario + ", Tierra de campeones!, tienes " + str(edadUsuario) + "años, debiste haber vivido un fuerte terremoto")

        if (origenUsuario == "Calama" or origenUsuario == "calama"):
            gaspar()
            print("Tierra de Sol y Cobre!")
            hb.hablarBot("Tierra de Sol y Cobre!")

        if (origenUsuario == "Coquimbo" or origenUsuario == "coquimbo"):
            gaspar()
            print("Puerto de los Piratas!")
            hb.hablarBot("Puerto de los Piratas!")

        if (origenUsuario == "Concepción" or origenUsuario == "concepción"):
            gaspar()
            print("La Perla del Bio-Bio")
            hb.hablarBot("La Perla del Bio-Bio")

        if (origenUsuario == "Valparaíso" or origenUsuario == "valparaíso"):
            gaspar()
            print("La Perla del Pacífico ")
            hb.hablarBot("La Perla del Pacífico ")

        if (origenUsuario == "Valdivia" or origenUsuario == "valdivia"):
            gaspar()
            print("La Perla del Sur")
            hb.hablarBot("La Perla del Sur")

    @Rule(estudio(estudResp="estudio1"))
    def estudio1(self):

        if (estudUsuario == "Informatico" and edadUsuario < 19):
            gaspar()
            print(nombreUsuario + " , todo un geek, pero esto recien comienza")
            hb.hablarBot(nombreUsuario + " , todo un geek, pero esto recien comienza")

        if (estudUsuario == "Informatico" and edadUsuario > 23):
            gaspar()
            print(nombreUsuario + " , un geek con experiencia")
            hb.hablarBot(nombreUsuario + " , un geek con experiencia")

        if (estudUsuario == "Industrial" and edadUsuario < 19):
            gaspar()
            print(nombreUsuario + " , cuidadito con dinamica! esto recien comienza")
            hb.hablarBot(nombreUsuario + " , cuidadito con dinamica! esto recien comienza")

        if (estudUsuario == "Industrial" and edadUsuario > 23):
            gaspar()
            print(nombreUsuario + " , ya deberias ser un experto en procesos")
            hb.hablarBot(nombreUsuario + " , ya deberias ser un experto en procesos")

        if (estudUsuario == "Geologia" and edadUsuario < 19):
            gaspar()
            print(nombreUsuario + " , eres todo un lamerocas")
            hb.hablarBot(nombreUsuario + " , eres todo un lamerocas")

        if (estudUsuario == "Geologia" and edadUsuario > 23):
            gaspar()
            print(nombreUsuario + " , un indiana jones")
            hb.hablarBot(nombreUsuario + " , un indiana jones")

        if (estudUsuario == "Fisica" and edadUsuario < 19):
            gaspar()
            print(nombreUsuario + " , estrellado")
            hb.hablarBot(nombreUsuario + " , estrellado")

        if (estudUsuario == "Fisica" and edadUsuario > 25):
            gaspar()
            print(nombreUsuario + " , estrellado de edad")
            hb.hablarBot(nombreUsuario + " , estrellado de edad")


        gaspar()
        print("¿De que ciudad vienes?")
        hb.hablarBot("¿De que ciudad vienes?")


