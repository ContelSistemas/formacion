# Escriba un programa que pida tres números y que escriba si son los tres iguales, si hay dos iguales o si son los tres distintos.

def compara():
    num1 = int(input("Introduce el pirmer número "))
    num2 = int(input("Introduce el segundo número "))
    num3 = int(input("Introduce el tercer número "))

    if num1 == num2 and num1 == num3 and num2 == num3:
        print ("Los tres numeros son iguales. ")
    elif num1 == num2 or num1 == num3 or num2 == num3:
        print ("Dos de esto numeros son iguales. ")
    else:
        print ("Todos los números son distintos")
compara()
