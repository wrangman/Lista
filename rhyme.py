
import random
import os    


def check_rhyme(what_rhyme, what_word):
    if what_rhyme == "light":
        if what_word in rhymes_used:
            return False    #word already used - no go!
        else:
            return True     #Word not used - go ahead        
    

def check_validity(what_rhyme, what_word):
    if what_rhyme == "light":
        if what_word in rhymes_light:
            return True    #word rhymes!
        else:
            return False     #Word does not rhyme
        
    
def ai_comment():
    ai_comments = ["Snyggt!",
                   "Bra, min tur...",
                   "Du hade tur där ;)",
                   "Bra gjort!",
                   "Fint!",
                   "OK, min tur...",
                   "Det var ett nytt ord!",
                   "Hm. Jag tänkte ta det ordet...",
                   "Sweet!"]
    
    comment_no = int(random.randrange(0, 8, 1))
    
    return ai_comments[comment_no]
    

def check_player(word):
    rhymes_used.append(word)

rhymes_light = ["knight",
                "bright",
                "flight",
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
                "kite",
                "rite",
                "spite",
                "quite",
                "fight"]

rhymes_used = []

os.system('cls')
total_light_words = 21
total_words_played = 0
current_rhyme = "light"
first_turn = True
selected_word = "light"


print("""
Välkommen till Rimspelet! ----------------------------------------------------
Välj ett ord du vill tävla i. Skriv ett rimmande ord (på en stavelse ej samma)
Om du kan fler ord än mig vinner du! Kan du inte fler ord tryck ENTER.\n""")

print(f"Ord som rimmar på {selected_word} - Lycka till!")
    
while True:
    if total_words_played == total_light_words:
        print("Jag vann - finns inga fler rim! Om du inte tror mig - kolla upp!")
        break
        
    while True:
        if first_turn:
            entry = input("Ord: ").lower()
        else:
            entry = input("Din tur: ").lower()
       
        entry = entry.replace(" ", "")
        
        if entry == "":
            print("Jag vann!")
            break
        
        if not check_validity(current_rhyme, entry):
            print("Det ordet rimmar inte - prova igen!\n")
            continue
        
        if check_rhyme(current_rhyme, entry):
            total_words_played += 1
            rhymes_used.append(entry)
            break
        else:
            print("Ordet har redan använts\n")
            continue
            
    first_turn = False
    
    if total_words_played >= total_light_words:
        print("Du vann - jag ger upp!")
        break
    

    while True:
        what_word = random.randrange(0, total_light_words, 1)
        ai_choice = rhymes_light[what_word]
        
        if ai_choice in rhymes_used:
            continue
        else:
            total_words_played += 1
            rhymes_used.append(ai_choice)
            break
        
    give_comment = ai_comment()
    print(f"{give_comment} Mitt ord: {ai_choice}")
             