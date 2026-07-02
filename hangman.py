import random

print("=" * 50)
print("🎮 WELCOME TO CODEALPHA HANGMAN GAME 🎮")
print("=" * 50)

print("\nRules:")
print("✔ Guess one letter at a time")
print("✔ You have 6 lives")
print("✔ Guess the word before your lives end")

input("\nPress Enter to Start...")

words = {
    "python": "A popular programming language",
    "computer": "An electronic machine",
    "keyboard": "Used for typing",
    "internet": "A worldwide network",
    "program": "A set of instructions",
    "variable": "Stores a value",
    "student": "A person who studies",
    "college": "A place for higher education"
}

secret_word = random.choice(list(words.keys()))
clue = words[secret_word]

print("\n💡 Clue:", clue)

display = []

for letter in secret_word:
    display.append("_")

print("Word:", " ".join(display))
stages = [
"""
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|   |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
 |   |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
     |
     |
     |
=========
""",
"""
 +---+
 |   |
     |
     |
     |
     |
=========
"""
]

lives = 6
wrong_letters = []
guessed_letters = []
score = 0
guess_count = 0
while "_" in display and lives > 0:

    print("\n" + "=" * 50)
    print("Word:", " ".join(display))
    print("❤️ Lives:", lives)
    print("🎯 Score:", score)
    print("🔢 Total Guesses:", guess_count)
    print("❌ Wrong Letters:", " ".join(wrong_letters))
    print(stages[lives])

    guess = input("\nGuess a letter: ").lower()

    if len(guess) != 1:
        print("❌ Please enter only ONE letter.")
        continue

    if not guess.isalpha():
        print("❌ Please enter only letters (A-Z).")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)
    guess_count += 1

    found = False

    for position in range(len(secret_word)):
        if secret_word[position] == guess:
            display[position] = guess
            found = True

    if found:
        score += 10
        print("✅ Correct!")
    else:
        lives -= 1
        score -= 2
        wrong_letters.append(guess)
        print("❌ Wrong Guess!")
        print("\n" + "=" * 50)

if "_" not in display:
    print("🎉 CONGRATULATIONS! 🎉")
    print("🏆 You Won!")
else:
    print("💀 GAME OVER!")
    print("The word was:", secret_word)

print("🎯 Final Score:", score)
print("🔢 Total Guesses:", guess_count)
print("=" * 50)