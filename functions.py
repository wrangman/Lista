# functions:  def!

def calculate(operator):
    if operator == "1" or operator == "+": print(x+y)
    if operator == "2" or operator == "-": print(x-y)
    if operator == "3" or operator == "*": print(x*y)
    if operator == "4" or operator == "/": print(x//y)
    

import os


# while och for?
#När ska man använda while / for?

user_value = input("hur många? ")

for i in range(user_value):
    print("coding is cool")



while True:
    os.system('cls')
    x = int(input("skriv tal x: "))
    y = int(input("skriv tal y: "))

    operator = input("Vill du plussa, minska, gångra, dela (1-4):")

    calculate(operator)
    again = input("nytt tal?")