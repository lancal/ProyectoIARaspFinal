# -*- coding: utf-8-*-

import keyboard

import subprocess

from escucharBot import *

from main import interaccionBot


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


        while True:

            global  proc1

            global  a

            a = True


            while keyboard.is_pressed("h"):

                if a == True:

                    proc1 = subprocess.Popen(args=['arecord', '--device=hw:0,0', '--format=S16_LE', 'TEMP.wav', '-c1', '-V mono'])

                    a = False


            if keyboard.is_pressed("h") is not True and a == False:

                print("dentro de if keyboard.h")

                proc1.kill()

                os.system("ffmpeg -i TEMP.wav -acodec pcm_s16le -ac 1 -ar 16000 tmp.wav")

                a = True

                sb = EscucharBot()

                sb.hablarBot()

                oraciones = self.leerArchivotempSTT()

                print(oraciones)
                print("oraciones line 102 conversacion.py")

                interaccionBot(oraciones)

                os.system("rm tempSTT/tempSTT.txt")

                os.system("rm tmp.wav")
