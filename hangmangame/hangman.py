import random

# Word list
words = ["apple", "tiger", "chair", "plant", "house","among","goury","bread", "train", "clock", "stone", "water","python", "java", "coding", "program", "debug",
    "laptop", "keyboard", "monitor", "printer", "router",
    "engine", "rocket", "planet", "galaxy", "astronaut",
    "doctor", "nurse", "police", "lawyer", "driver",
    "market", "office", "factory", "company", "manager",
    "happy", "angry", "brave", "smart", "quick"]

# Random word selection
word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_attempts = 6

# Hangman stages
stages = [
"""
-----
|   |
    |
    |
    |
    |
=========
""",
"""
-----
|   |
O   |
    |
    |
    |
=========
""",
"""
-----
|   |
O   |
|   |
    |
    |
=========
""",
"""
-----
|   |
O   |
/|  |
    |
    |
=========
""",
"""
-----
|   |
O   |
/|\\ |
    |
    |
=========
""",
"""
-----
|   |
O   |
/|\\ |
/   |
    |
=========
""",
"""
-----
|   |
O   |
/|\\ |
/ \\ |
    |
=========
"""
]

print("Welcome to Hangman!")

while wrong_guesses < max_attempts:
    
    print(stages[wrong_guesses])
    
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    print("Word:", display_word.strip())
    
    if "_" not in display_word:
        print("You guessed the word correctly!")
        break
    
    guess = input("Enter a letter: ").lower()
    
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue
    
    guessed_letters.append(guess)
    
    # Check guess
    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print(f"Wrong guess! Attempts left: {max_attempts - wrong_guesses}")

# Final result
if wrong_guesses == max_attempts:
    print(stages[wrong_guesses])
    print("Game Over! The word was:", word)
