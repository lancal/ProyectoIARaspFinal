# -*- coding: utf-8-*-

import keyboard

from subprocess import Popen,PIPE

from escucharBot import *

from main import interaccionBot

from os import devnull

import re

from termios import tcflush, TCIFLUSH

import sys


class Conversacion(object):


    def leerArchivotempSTT(self):

        global oraciones


        with open("tempSTT/tempSTT.txt","r") as f:

            oraciones = f.readline()


        return oraciones


    def handleForever(self):

        print("Gaspar:")
        print("Hola mi nombre es Gaspar")
        print("------------------------")
        print("Usuario Habla: ")


        while True:

            global  proc1

            global  a

            a = True


            while keyboard.is_pressed("h"):

                if a == True:

                    proc1 = Popen(args=['arecord', '--device=hw:0,0', '--format=S16_LE', 'TEMP.wav', '-c1', '-V mono'],
                                  stdout=PIPE, stderr=PIPE)

                    #print('proc2\'s pid=', proc1.pid)

                    a = False

            if keyboard.is_pressed("e"):

                tcflush(sys.stdin,TCIFLUSH)

                print("Ahora puedes Escribir algo a Gaspar")

                usuario = input("Escribe algo a Gaspar :) \n")

                interaccionBot(usuario)

                if usuario == "salir":

                    break

            if keyboard.is_pressed("h") is not True and a == False:

                tcflush(sys.stdin,TCIFLUSH)


                #print("dentro de if keyboard.h")

                proc1.kill()

                #os.system("ffmpeg -i TEMP.wav -acodec pcm_s16le -ac 1 -ar 16000 tmp.wav")

                proc2 = Popen(args=['ffmpeg','-i','TEMP.wav','-acodec','pcm_s16le','-ac','1','-ar','16000','tmp.wav'],
                              stdout=PIPE, stderr=PIPE)

                #(out, err) = proc2.communicate()

                #print('proc2\'s pid=',proc2.pid)

                a = True

                print("\nGaspar esta analizando lo que dijiste :) ")

                sb = EscucharBot()

                sb.hablarBot()

                oraciones = self.leerArchivotempSTT()

                print(oraciones)
                #print("Tu dijiste: " + oraciones)

                interaccionBot(oraciones)

                os.system("rm tempSTT/tempSTT.txt")

                os.system("rm tmp.wav")

                patron = re.compile(r'(salir)', re.I)
                m_match = patron.match(oraciones)

                if m_match:

                    m_match = str((m_match.group(1)))

                    if isinstance(m_match, str):

                        break

