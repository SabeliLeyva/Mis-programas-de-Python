#MODULO 1

#Ejercicio 1. Dia actual
from datetime import date
from re import template

print("Hoy es: " + str(date.today()))

#Ejercicio 2. Convertidor de parsec a años luz
parsec = input("\nIngresa el numero de parsecs a conertir: ")
anios_luz = int(parsec) * 3.26156
print("" + str(parsec) + " parsecs en años luz son: " + str(anios_luz))

#MODULO 3
size_asteroid = 6
speed_asteroid = 15
entro_atmosfera = 'si'
choque = 'no'
if size_asteroid > 25 and size_asteroid < 1000 and choque == 'no':
    print("Por poco y valimos chetos")
elif choque == 'si' and speed_asteroid >= 20 and entro_atmosfera == 'si':
    print("Ya valio queso, llamen a Bruce Willis")
elif entro_atmosfera == 'si' and choque == 'no' :
    print("Mendiga piedra me saco un... suspiro!!!")
else :
   print("Todo bien, no hay pe... ligro!!!")

#MODULO 4
#Ejercicio 1
text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""
print(text.split("."))

Claves = ['facts', 'temperature', 'satellite', 'moves', 'distance']

for sentence in text :
    for cve in Claves :
        if cve in sentence : 
            print(sentence)
            break

Claves = ['C']

for sentence in text :
    for cve in Claves :
        if cve in sentence : 
            print(sentence.replace('C', 'Celsius'))
            break

#Ejercicio 2
nombre = "Luna"
gravedad = 0.00162
planeta = "Tierra"

titulo = f'\nGravedad sobre la {planeta} y la {nombre} \n'.title()

hechos = f"""{'-' * 60}
Nombre del planeta: {planeta}
Gravedad en la {nombre}: {gravedad * 1000} m/s """

template = f"""{titulo}{hechos}"""

print(template)

planeta1 = 'Marte '
gravedad1  = 0.00143
nombre1 = 'Ganimedes'