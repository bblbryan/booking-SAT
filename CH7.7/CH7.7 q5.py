import sys

user_input = input("Type 'yes' to continue: ")

if user_input.lower() != "yes":
    print("Invalid input. Exiting program.")
    sys.exit(1) # Exit with an error code
else:
    print("Continuing the program...")
    # ... rest of the program ...