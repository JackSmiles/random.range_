import random

firtsNumber = input("Añade un numero y lo adivinare del 1 al 10 : ")
randomRange = random.randint(1, 10)

def adivina():
    if int(firtsNumber) > 10:
        print("No puede ser mayor a 10!")

    if randomRange == int(firtsNumber):
        print(f"¡Adivine el numero! El numero es {int(firtsNumber)}")
    else:
        print(f"No pude adivinar el numero, mi numero es : {int(randomRange)}")

adivina()
