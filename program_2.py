# Program #2: Word Separator
# Write a program that accepts as input a sentence in which all of the words are run together, 
# but the first character of each word is uppercase.  
# Convert the sentence to a string in which the words are separated by spaces, 
# and the first word starts with an uppercase.  
# For example the string "StopAndSmellTheRoses" would be converted to "Stop and smell the roses."

# Start your changes on line 13

def main():
    text = input("Enter a concatenated sentence (e.g., StopAndSmellTheRoses): ")

    result = text[0]  # first letter stays uppercase

    for char in text[1:]:
        if char.isupper():
            result += " " + char.lower()
        else:
            result += char

    print("Separated sentence:", result)

if __name__ == "__main__":
    main()
