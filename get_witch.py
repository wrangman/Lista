from msvcrt import getwch


while True:
    print("Tryck N för att sluta")
    press = getwch().upper()
    
    if press == "N": 
        exit()
    else:
        continue
    


