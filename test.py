import random
import textwrap
# Simple terminal Hangman-style word game.
# Run: python game.py
# Guess letters until the word is revealed.
# Too many wrong guesses ends the game.
WORDS = ["python", "variable", "function", "compiler", "network", "algorithm", "database"]
STAGES = [
    "  +---+\n      |\n      |\n      |\n     ===",
    "  +---+\n  O   |\n      |\n      |\n     ===",
    "  +---+\n  O   |\n  |   |\n      |\n     ===",
    "  +---+\n  O   |\n /|\\  |\n      |\n     ===",
    "  +---+\n  O   |\n /|\\  |\n / \\  |\n     ===",
]
def pick_word():
    return random.choice(WORDS)
def show_state(secret, guessed):
    return " ".join(c if c in guessed else "_" for c in secret)
def prompt_letter():
    while True:
        s = input("Guess a letter: ").strip().lower()
        if len(s) == 1 and s.isalpha():
            return s
        print("Please enter a single letter.")
def main():
    secret = pick_word()
    guessed, wrong = set(), 0
    max_wrong = len(STAGES) - 1
    msg = "Word Guess! You have limited wrong guesses. Type letters to reveal the word."
    print(textwrap.fill(msg, 70))
    while True:
        print("\n" + STAGES[wrong])
        print("Word:", show_state(secret, guessed))
        print("Guessed:", " ".join(sorted(guessed)) or "(none)", "| Wrong:", wrong, "/", max_wrong)
        if all(c in guessed for c in secret):
            print("You win! The word was:", secret)
            return
        if wrong >= max_wrong:
            print("You lose! The word was:", secret)
            return
        ch = prompt_letter()
        if ch in guessed:
            print("Already guessed.")
            continue
        guessed.add(ch)
        if ch not in secret:
            wrong += 1
            print("Nope!")
if __name__ == "__main__":
    main()