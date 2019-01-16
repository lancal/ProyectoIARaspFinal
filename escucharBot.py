import os

from subprocess import Popen,PIPE

class EscucharBot(object):

    def hablarBot(self):

        #with open("hablarBot.txt", "w") as arch:
            #arch.write(conversacion)

        #os.system("espeak -f hablarBot.txt -v spanish-latin-am -s 130 -p 50")

        os.system("gcc -o test test.c -DMODELDIR=\"`pkg-config --variable=/home/pi/ProyectoIA/sphinx/ pocketsphinx`\" `pkg-config --cflags --libs pocketsphinx sphinxbase`")
        #os.system("./test")


        proc1 = Popen(args=['./test'],stdout=PIPE, stderr=PIPE)

        print("Tu dijiste: ")

        (out, err) = proc1.communicate()

        os.system("rm test")