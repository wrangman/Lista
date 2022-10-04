
min_lista = [1, 2, 3, 4]      # skapa en lista
max = min_lista[0]            # sätt en variabel som
                            # innehåller första talet i
                            # listan (0)

for i in min_lista:           # for-loop
    if i > max:               # om talet är större än talet i
        max = i               # max-variabeln lägg in det talet

print(max)                    # skriv ut max som ska innehålla
                                #det största talet
