rhymes_light = ["knight",
                "bright",
                "fright",
                "flight",
                "fight",
                "night",
                "shite",
                "blight",
                "right",
                "tight",
                "sight",
                "white",
                "plight",
                "slight",
                "might",
                "height",
                "tight",
                "nite",
                "bite",
                "pike",
                "kite",
                "rite",
                "lite",
                "cite",
                "spite",
                "trite",
                "quite",
                "bight",
                "byte",
                "brite",
                "dwight",
                "leyte",
                "mite",
                "site",
                "sleight",
                "smite",
                "spite",
                "sprite",
                "trite",
                "wright",
                "write"]


tot = len(rhymes_light)

print(tot)
coun = 0
for i in rhymes_light:
    coun += 1
    print("rhyme: " + str(coun) +  ": " + i)

print("\n")

seen = set()
uniq = []
notuniq = []
for x in rhymes_light:
    if x not in seen:
        uniq.append(x)
        seen.add(x)
    else:
        notuniq.append(x)


print(notuniq)