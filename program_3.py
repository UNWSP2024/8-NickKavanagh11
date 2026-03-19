# Program #3: Capital Quiz
# Write a program that creates a dictionary containing the U.S. states as keys, 
# and their capitals as values.  
# The program should then randomly quiz the user by displaying the name of a state 
# and asking the user to enter the state's capital.  
# The program should count of the number of correct and incorrect responses.  
# (You could alternatively use another country and provinces, 
# or countries of the world and capitals).

import random

def main():
    states = {
        "Minnesota": "Saint Paul",
        "California": "Sacramento",
        "Texas": "Austin",
        "Florida": "Tallahassee",
        "New York": "Albany"
    }

    correct = 0
    incorrect = 0

    for _ in range(5):  # ask 5 questions
        state = random.choice(list(states.keys()))
        answer = input(f"What is the capital of {state}? ")

        if answer.strip().lower() == states[state].lower():
            print("Correct!")
            correct += 1
        else:
            print(f"Incorrect. The correct answer is {states[state]}.")
            incorrect += 1

    print("\nQuiz Results:")
    print("Correct answers:", correct)
    print("Incorrect answers:", incorrect)

if __name__ == "__main__":
    main()
