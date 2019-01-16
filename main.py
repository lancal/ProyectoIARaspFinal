#!/usr/bin/python3
# -*- coding: utf-8-*-

from iBot import *

from conversacion import *

import re
from random import choice

from hablarBot import *

from escucharBot import *

resUsuario = ""

class Gaspar(object):

    def run(self):

        saludoInicial = "Hola mi nombre es Gaspar, como te llamas?"

        hb = HablarBot()
        hb.hablarBot(saludoInicial)

        conversation = Conversacion()
        conversation.handleForever()

    def main(self):

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

            if resUsuario == "chao":
                cerrar = False


def interaccionBot(respUsuario):

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

    if m_match:

        asdf = str((m_match.group(1)))

        setNombre(asdf)

        c = choice(['nombre1'])
        engine = respuestasBot()
        engine.reset()
        engine.declare(nombre(nombreResp=c))
        engine.run()

    else:

        pass

    if resUsuario == "chao":

        hb = HablarBot()
        hb.hablarBot("Chao\n")

        print("\nChao :( \n")

    if resUsuario == "1":

        sb = EscucharBot()
        sb.hablarBot()

    print("------------------------")


if __name__ == "__main__":

    print("*******************************************************")
    print("*             Gaspar - El Chatbot Inteligente         *")
    print("* (c) 2019 Alan Calderon, Manuel Caceres              *")
    print("*******************************************************")


    app = Gaspar()


    app.run()