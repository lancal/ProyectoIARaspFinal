import os

from subprocess import Popen,PIPE

class EscucharBot(object):

    def hablarBot(self):

        #with open("hablarBot.txt", "w") as arch:
            #arch.write(conversacion)

        #os.system("espeak -f hablarBot.txt -v spanish-latin-am -s 130 -p 50")

        os.system("gcc -o test test.c -DMODELDIR=\"`pkg-config --variable=/home/pi/ProyectoIA/sphinx/ pocketsphinx`\" `pkg-config --cflags --libs pocketsphinx sphinxbase`")
        #os.system("./test")

        #print("LINE 17")

        proc1 = Popen(args=['./test'],stdout=PIPE, stderr=PIPE)

        print("Tu dijiste: ")

        (out, err) = proc1.communicate()

        #print("Tu dijiste: " + str(out))

        #print("LINE 23")

        #stout = proc1.stdout

        #print(stout)

        #print("Tu dijiste: " + str(out))

        #print("cat returned code = %d" % proc1.returncode)
        #print("cat output:\n\n%s\n\n" % out)
        #print("cat errors:\n\n%s\n\n" % err)

        os.system("rm test")