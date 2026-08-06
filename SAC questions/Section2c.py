import random
import string

play = input("Would you like to start playing?:")

if play.strip().lower() in ["y", "yes"]:
    print("Great! Let's start playing!")
    print("Your staring word is begin")
else:
    print("Goodbye!")
    exit()

random_letters = ''.join(random.choices(string.ascii_lowercase, k=10))
start_word = "begin" + random_letters
print("Here are you 10 random letters ", start_word)

