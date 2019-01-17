#!/usr/bin/python3
# -*- coding: utf-8-*-

from iBot import *

from conversacion import *

import re
from random import choice

from varios import *

resUsuario = ""

class Gaspar(object):

    def run(self):

        saludoInicial = "Hola mi nombre es Gaspar, como te llamas?"

        hb = HablarBot()
        hb.hablarBot(saludoInicial)

        conversation = Conversacion()
        conversation.handleForever()

def main():

    global resUsuario
    cerrar = True

    print("Gaspar:")
    print("Hola mi nombre es Gaspar")
    print("------------------------")
    while cerrar != False:
        print("Usuario")
        resUsuario = input()
        print("------------------------")
        interaccionBot(resUsuario)

        if resUsuario == "salir":
            cerrar = False


def interaccionBot(respUsuario):

<<<<<<< HEAD
    #print(respUsuario)
    #print("respUsuario")
=======
    global a

    print(respUsuario)
    print("respUsuario")
>>>>>>> a514a62bb8fa24fbc50b27f43916c78e23a69f23

    varios = Varios()
    hb = HablarBot()

    patron = re.compile(r'hola', re.I)
    arreglo = patron.findall(str(respUsuario))
    #print("Gaspar:")
    if arreglo.__len__() == 1:
        if resUsuario == arreglo[0]:
            c = choice(['saludo1', 'saludo2'])
            engine = respuestasBot()
            engine.reset()
            engine.declare(saludo(saludos=c))
            engine.run()

    patron = re.compile(r'que hay del tiempo', re.I)
    arreglo = patron.findall(str(respUsuario))

    if arreglo.__len__() == 1:
        if resUsuario == arreglo[0]:
            c = choice(['nublado', 'soleado'])
            engine = respuestasBot()
            engine.reset()
            engine.declare(tiempo(tiempos=c))
            engine.run()

    patron = re.compile(r'mi nombre es (.*)', re.I)
    m_match = patron.match(respUsuario)

    a = False

    if m_match:



        asdf = str((m_match.group(1)))

        setNombre(asdf)

        c = choice(['nombre1'])
        engine = respuestasBot()
        engine.reset()
        engine.declare(nombre(nombreResp=c))
        engine.run()

        a = True

    else:

        pass

    patron = re.compile(r'(dime la hora|que edad tienes|salir)',re.I)
    m_match = patron.match(respUsuario)

<<<<<<< HEAD
    global a

=======
>>>>>>> a514a62bb8fa24fbc50b27f43916c78e23a69f23
    if m_match:

        m_match= str((m_match.group(1)))

        if isinstance(m_match,str):

            a = varios.buscarRespuesta(m_match)

    elif m_match and a == True:

        gaspar()
        print("No entiendo lo que dices")
        hb.hablarBot("No entiendo lo que dices")

        a = False

    # -------posminombre
    patron = re.compile(r'tengo (.*) años', re.I)
    m_match = patron.match(respUsuario)

    # if isinstance(patron.match(respUsuario),int):


    if m_match:

        edadUser = int((m_match.group(1)))
        #int(edadUser)
        setEdad(edadUser)
        engine = respuestasBot()
        engine.reset()
        engine.declare(edad(edadResp='edad1'))
        engine.run()


    patron = re.compile(r'estoy estudiando (.*)', re.I)
    m_match = patron.match(respUsuario)

    if m_match:
        estudUsuario = str((m_match.group(1)))
        setEstudio(estudUsuario)
        engine = respuestasBot()
        engine.reset()
        engine.declare(estudio(estudResp='estudio1'))
        engine.run()

    patron = re.compile(r'soy de (.*)')
    m_match = patron.match(respUsuario)
    if m_match:
        origenUsuario = str((m_match.group(1)))
        setOrigen(origenUsuario)
        engine = respuestasBot()
        engine.reset()
        engine.declare(origen(origenResp='origen1'))
        engine.run()
    # --------Salir


if __name__ == "__main__":

    print("*******************************************************")
    print("*             Gaspar - El Chatbot Inteligente         *")
    print("* (c) 2019 Alan Calderon, Manuel Caceres              *")
    print("*******************************************************")


    app = Gaspar()

    app.run()
