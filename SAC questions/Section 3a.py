play = input("Would you like to create a list?:")

if play.strip().lower() in ["y", "yes"]:
    print("Let's create a list!")
else:
    print("Goodbye!")
    exit()