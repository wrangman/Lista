import random


eng6 = ["Max",
        "Jack",
        "Morris",
        "Ritvars",
        "Hampus",
        "Benjamin",
        "Svante",
        "Fred",
        "Simon",
        "Valdemar",
        "Assar",
        "Johan",
        "Aleksandrs",
        "Oliver",
        "Mandus",
        "Oscar",
        "Elliot",
        "Melvin",
        "Axel",
        "Maksymilian",
        "Theo",
        "Cris",
        "Victor",
        "Dexter",
        "Alexander",
        "William",
        "Bartoz"]

temp = []

for i in range(len(eng6)):
    pupil = random.randint(0, len(eng6) - 1)
    temp.append(eng6[pupil])
    eng6.pop(pupil)

print("-" * 20)

print("Total students: " + str(len(temp)))
print("-" * 20)

for i in range(len(temp)):
    print(temp[i])

'''

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