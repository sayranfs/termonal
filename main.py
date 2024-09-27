# Initial imports and variable values.
import json
import random as rd

response = ""

# Opening the archive of words,
with open('list.json', 'r') as file:
    file = json.load(file)
    words = file["words"]
    win_messages = file["winMessages"]

# Choosing a random word.
selected_word = rd.choice(words)
sliced_selected_word = list(selected_word)

# Introducing.
print("____________________ Welcome to the ____________________")
print("""___________                                       .__   
\\__    ___/__________  _____   ____   ____ _____  |  |  
  |    |_/ __ \\_  __ \\/     \\ /  _ \\ /    \\\\__  \\ |  |  
  |    |\\  ___/|  | \\/  Y Y  (  <_> )   |  \\/ __ \\|  |__
  |____| \\___  >__|  |__|_|  /\\____/|___|  (____  /____/
             \\/            \\/            \\/     \\/      
\n\n""")

print("A random 5 letter word has been selected for you, discover it. MUAHAHAHA 😈😈😈")
print("""
+ CORRECT
- WRONG POSITION
x WRONG
""")

# Code...
for i in range(5):

    sliced_attempt = list(input(""))
    set_sliced_attempt = set(sliced_attempt)
    set_sliced_selected_word = set(sliced_selected_word)
    upper_intersection = [letter.upper() for letter in (set_sliced_attempt & set_sliced_selected_word)]

    for x, letter in enumerate(sliced_attempt):
        if letter.upper() == sliced_selected_word[x].upper():
            response += "+"
        elif letter.upper() in upper_intersection:
            response += "-"
        else:
            response += "x"

    print(response + "\n" if response != "+"*5 else rd.choice(win_messages))
    if response == "+"*5: break;
    response = ""

print(f"YOU LOST :( The word was >>> {selected_word.upper()} <<< Don't be discouraged, try again!" if response != "+"*5 else "")