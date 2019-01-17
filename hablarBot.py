import os

class HablarBot(object):

    def hablarBot(self,conversacion,extra=None):

        if extra is not None:
            with open("hablarBot.txt", "w") as arch:
                arch.write(conversacion)
                arch.write("\t")
                arch.write(extra)

        else:

            with open("hablarBot.txt", "w") as arch:
                arch.write(conversacion)

        os.system("espeak -f hablarBot.txt -v spanish-latin-am -s 130 -p 50")

        os.system("rm hablarBot.txt")

