rhymes_light = ["knight",
              "wright",
              "bright",
              "fright",
            "flight",
            "fight",
            "night",
            "shite",
            "blight",
            "right",
            "blite",
            "tight",
            "sight",
            "white",
            "plight",
            "slight",
            "flite",
            "might",
            "height",
            "leyte",
            "nite",
            "aiit",
            "bite",
            "kite",
            "rite",
            "lite",
            "cite",
            "spite",
            "trite",
            "quite",
            "dight",
            "cyte",
            "bight",
            "byte",
            "mite",
            "site",
            "sleight",
            "smite",
            "sprite",
            "twite",
            "wight",
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


if notuniq: 
    print(notuniq)
else:
    print("no dupes! :)")