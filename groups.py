import random


eng6 = [["Max", 3],
        ["Jack", 5],
        ["Morris", 5],
        ["Ritvars", 3],
        ["Hampus", 3],
        ["Benjamin", 4],
        ["Svante", 4],
        ["Fred", 3],
        ["Simon", 4],
        ["Valdemar", 4],
        ["Assar", 3],
        ["Johan", 4],
        ["Aleksandrs", 2],
        ["Oliver", 3],
        ["Mandus", 3],
        ["Oscar", 2],
        ["Elliot", 3],
        ["Melvin", 5],
        ["Axel", 4],
        ["Maksymilian", 2],
        ["Theo", 3],
        ["Cris", 5],
        ["Victor", 3],
        ["Dexter", 4],
        ["Alexander", 2],
        ["William", 2],
        ["Bartoz", 2]]

temp = []

tot1 = 0
tot2 = 0
tot3 = 0
tot4 = 0
tot5 = 0

for i in range(len(eng6)):
    if eng6[i][1] == 1:
        tot1 += 1
    elif eng6[i][1] == 2:
        tot2 += 1
    elif eng6[i][1] == 3:
        tot3 += 1
    elif eng6[i][1] == 4:
        tot4 += 1
    elif eng6[i][1] == 5:
        tot5 += 1


for i in range(len(eng6)):
    pupil = random.randint(1, len(eng6))
    temp.append(eng6[pupil])






print("-" * 15)
print("Total students: " + str(len(temp)))
print("-" * 15)



for i in range(len(temp)):
    print(temp[i])


'''

for i in range(int(len(eng6))):
    if eng6[i][1] == 1: 
        group1.append(eng6[i])
    elif eng6[i][1] == 2: 
        group2.append(eng6[i])
    elif eng6[i][1] == 3: 
        group3.append(eng6[i])
    elif eng6[i][1] == 4: 
        group4.append(eng6[i])
    elif eng6[i][1] == 5: 
        group5.append(eng6[i])
    



print("GROUP 1:")
for i in range(len(group1)):
    print(group1[i])

print("GROUP 2:")
for i in range(len(group2)):
    print(group2[i])

print("GROUP 3:")
for i in range(len(group3)):
    print(group3[i])

print("GROUP 4:")
for i in range(len(group4)):
    print(group4[i])

print("GROUP 5:")
for i in range(len(group5)):
    print(group5[i])



'''