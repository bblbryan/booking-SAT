play = input("Would you like to start playing?:")

if play.strip().lower() in ["y", "yes"]:
    print("Great! Let's start playing!")
else:
    print("Goodbye!")
    exit()

