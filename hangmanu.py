import random
word_list = [
    ("python", "Programming Language"),
    ("elephant", "Largest land animal"),
    ("rainbow", "Appears after rain"),
    ("diamond", "A precious stone"),
    ("volcano", "Mountain that erupts")
]
secret_word, hint = random.choice(word_list)
guessed = []
wrong = 0
score = 100
max_wrong = 6
print("=" * 45)
print("🎮 WELCOME TO HANGMAN ADVENTURE 🎮")
print("=" * 45)
print("Guess the secret word one letter at a time!")
print("You can make only 6 wrong guesses.")
print("⭐ Starting Score:", score)
print()
while wrong < max_wrong:
    display = ""
    for letter in secret_word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    print("\nWord :", display)
    print("💡 Hint :", hint)
    print("❌ Wrong Guesses Left :", max_wrong - wrong)
    print("⭐ Score :", score)
    if "_" not in display:
        print("\n🏆 Congratulations!")
        print("You guessed the word:", secret_word.upper())
        print("Final Score:", score)
        break
    guess = input("\nEnter a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter only one alphabet.")
        continue
    if guess in guessed:
        print("🔁 You already guessed that letter.")
        continue
    guessed.append(guess)
    if guess in secret_word:
        print("✅ Great! Correct letter.")
        score += 10
    else:
        print("❌ Oops! Wrong letter.")
        wrong += 1
        score -= 10
if wrong == max_wrong:
    print("\n💀 GAME OVER!")
    print("The secret word was:", secret_word.upper())
    print("Final Score:", score)