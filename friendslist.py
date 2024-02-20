'''
FRIENDSLIST.PY: En vänlista med list-funktionen

__author__  = "Johan Wrangö"
__version__ = "1.0.0"
__email__   = "johan.wrango@ntig.se"
'''

import os


def show_friends():
    os.system('cls')
    print("-------- MINA VÄNNER --------")
    for i, name in enumerate(friends_list):
        print(f"{i+1}) {name}")
        
    print(f"\nAntal vänner: {len(friends_list)}\n")


def rename(f_index, f_name):
    if friends_list[f_index] != f_name and f_name != "":
        friends_list[f_index] = f_name


def custom_text(friends_list):
    if len(friends_list) > 1:
        return f"Lägg till/Ta bort/Ändra (1-{str(len(friends_list))}): "
        
    elif len(friends_list) > 0:
        return "Lägg till/Ta bort/Ändra: "

    elif len(friends_list) > -1:
        return "Lägg till en ny vän: "


# Här börjar programmet
os.system('cls')

friends_list = []

print("""
------ MINA BÄSTA VÄNNER  ------
Lägg till vän - skriv nytt namn
Ta bort vän - skriv samma namn
Ändra namn - välj nummer i lista
---------------------------------
                   Avsluta med /q
---------------------------------""")

while True:
    modify = input(custom_text(friends_list))

    if modify.upper() == "/QUIT" or modify.upper() == "/Q":                # Avsluta
        break
    if not modify.isdigit():
        try:
            friends_list.remove(modify)         # Ta bort vän
            show_friends()
        except ValueError:                      # Vännen fanns ej - lägg till
            if modify != "": friends_list.append(modify)
            show_friends()
            continue
    elif modify.isdigit():
        try:
            if int(modify) > 0:                 # Ändra namn
                cf = input(f"Ändra '{friends_list[int(modify)-1]}' till: ")
                rename(int(modify)-1, cf)
                show_friends()
        except IndexError:                      # Vännen fanns ej - kunde inte ändras
            continue
