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
print("Here are your 10 random letters", start_word)

user_word = input("Type your first word using at least one letter from 'begin' and one from the random letters: ").lower()

users_begin_letter = any(letter in start_word for letter in user_word)
users_random_letter = any(letter in random_letters for letter in user_word)

