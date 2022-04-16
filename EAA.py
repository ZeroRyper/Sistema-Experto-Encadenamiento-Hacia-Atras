
import pymongo
from conncM import *

result1=coleccion.find_one({"nombreenf":"Bronquitis aguda"})
result2=coleccion.find_one({"nombreenf":"Resfriado común"})
result3=coleccion.find_one({"nombreenf":"Infección de oído"})

cons=input("Consulta y/n ")

if(cons=="y"):
    print("Tienes Tos y/n?")
    sin1=input()
    if(sin1=="y"):
        print("Tienes dolor de pecho y/n?")
        sin3=input()
        if(sin3=="y"):
            print(result1)
        else:
            print(result2)
    else:
        print("Tienes dolor de oido y/n?")
        sin2=input()
        if(sin2=="y"):
            print(result3)
        else:
            print('Consulta a tu medico')


else:
    print('Fin')
