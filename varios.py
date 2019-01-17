import datetime

from hablarBot import *

from iBot import *

class Varios(object):

    def hora(self):

        x = datetime.datetime.now()

        #print(x.year)
        #print(x.hour)
        #print(x.minute)

        hora = x.hour
        minuto = x.minute

        return hora,minuto

    def buscarRespuesta(self,respUsuario):

        # print(respUsuario)
        # print("respUsuario line 142")

        if respUsuario == "que edad tienes":

            hb = HablarBot()
            gaspar()

            print("no tengo edad soy un bot inteligente")
            hb.hablarBot("no tengo edad soy un bot inteligente")

        if respUsuario == "dime la hora":

            hb = HablarBot()
            gaspar()

            hora, minuto = self.hora()

            print("Son las " + str(hora) + " horas con " + str(minuto) + " minutos")
            hb.hablarBot("son las " + str(hora) + " horas con" + str(minuto) + " minutos")

        if respUsuario == "salir":

            hb = HablarBot()
            gaspar()
            print("Hasta la proxima :) ")
            hb.hablarBot("hasta la proxima")

            print("\nTerminando conversacion :( ")
            print("------------------------")

        else:

            print("------------------------")
            print("Usuario Habla: ")


        # hb = HablarBot()
        # gaspar()
        # hb.hablarBot("No entiendo lo que dices")
