# Program #1: Initials
# Write a program that gets a string containing a person's first, middle, and last names, 
# and displays their first, middle, and last initials.  
# For example, if the user enters John William Smith, the program should display J. W. S.

# Add your logic starting on line 11

def main():
    full_name = input("Enter your first, middle, and last name: ")

    names = full_name.split()

    if len(names) >= 3:
        initials = f"{names[0][0].upper()}. {names[1][0].upper()}. {names[2][0].upper()}."
        print("Initials:", initials)
    else:
        print("Please enter first, middle, and last names.")

if __name__ == "__main__":
    main()
