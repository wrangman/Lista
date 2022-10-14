def showCandy():
    for i in candy_bars:
        print(i)


import os
os.system('cls')


my_list = [1.5, 2, 3, 4]      # skapa en lista
                            # innehåller första talet i
                            # listan (0)

candy_bars = ["kexchoklad", "sport lunch", "snickers", "sport bar", "geisha", "mars", "twix", "milky way"]


#print(candy_bars)

showCandy()

new_bar = input("En till choklad? ")

candy_bars.append(new_bar)

showCandy()

remove_bar = input(f"Ta bort choklad? 1-{len(candy_bars)-1}")

candy_bars.pop(int(remove_bar))

showCandy()

'''
for i in min_lista:           # for-loop
    if i > max:               # om talet är större än talet i
        max = i               # max-variabeln lägg in det talet

print(max)                    # skriv ut max som ska innehålla
                                #det största talet
'''