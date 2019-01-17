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

    global a

    global abc

    varios = Varios()
    hb = HablarBot()

    abc = False

    patron = re.compile(r'(hola)', re.I)
    m_match = patron.match(respUsuario)
    #arreglo = patron.findall(str(respUsuario))

    #print("Gaspar:")
    if m_match and abc == False:

            m_match = str((m_match.group(1)))

            if isinstance(m_match, str):

                c = choice(['saludo1', 'saludo2'])
                engine = respuestasBot()
                engine.reset()
                engine.declare(saludo(saludos=c))
                engine.run()

                a = True

    patron = re.compile(r'(que hay del tiempo)', re.I)
    #arreglo = patron.findall(str(respUsuario))
    m_match = patron.match(respUsuario)

    if m_match and abc == False:

        m_match = str((m_match.group(1)))

        if isinstance(m_match, str):

            c = choice(['nublado', 'soleado'])
            engine = respuestasBot()
            engine.reset()
            engine.declare(tiempo(tiempos=c))
            engine.run()

            abc = True

    patron = re.compile(r'mi nombre es (.*)', re.I)
    m_match = patron.match(respUsuario)

    if m_match and abc == False:

        asdf = str((m_match.group(1)))

        setNombre(asdf)

        c = choice(['nombre1'])
        engine = respuestasBot()
        engine.reset()
        engine.declare(nombre(nombreResp=c))
        engine.run()

        abc = True

    else:

        pass

    patron = re.compile(r'(dime la hora|que edad tienes|salir)',re.I)
    m_match = patron.match(respUsuario)

    if m_match and abc == False:

        m_match= str((m_match.group(1)))

        if isinstance(m_match,str):

            a = varios.buscarRespuesta(m_match)

            abc = True

    elif m_match and abc == False:

        gaspar()
        print("No entiendo lo que dices")
        hb.hablarBot("No entiendo lo que dices")

        abc = True

    # -------posminombre
    patron = re.compile(r'tengo (.*) años', re.I)
    m_match = patron.match(respUsuario)

    # if isinstance(patron.match(respUsuario),int):


    if m_match and abc == False:

        edadUser = int((m_match.group(1)))
        #int(edadUser)
        setEdad(edadUser)
        engine = respuestasBot()
        engine.reset()
        engine.declare(edad(edadResp='edad1'))
        engine.run()

        abc = True


    patron = re.compile(r'estoy estudiando (.*)', re.I)
    m_match = patron.match(respUsuario)

    if m_match and abc == False:
        estudUsuario = str((m_match.group(1)))
        setEstudio(estudUsuario)
        engine = respuestasBot()
        engine.reset()
        engine.declare(estudio(estudResp='estudio1'))
        engine.run()

        abc = True

    patron = re.compile(r'soy de (.*)')
    m_match = patron.match(respUsuario)

    if m_match and abc == False:
        origenUsuario = str((m_match.group(1)))
        setOrigen(origenUsuario)
        engine = respuestasBot()
        engine.reset()
        engine.declare(origen(origenResp='origen1'))
        engine.run()

        abc = True
    # --------Salir

    if respUsuario and abc == False:
        c = choice(['1', '2', '3'])
        engine = respuestasBot()
        engine.reset()
        engine.declare(defectoPor(defectoResp=c))
        engine.run()

        abc = True



if __name__ == "__main__":

    print("*******************************************************")
    print("*             Gaspar - El Chatbot Inteligente         *")
    print("* (c) 2019 Alan Calderon, Manuel Caceres              *")
    print("*******************************************************")


    app = Gaspar()

    app.run()
