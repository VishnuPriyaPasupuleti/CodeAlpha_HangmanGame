import random
words = {
    "python": "A popular programming language",
    "mango": "A sweet tropical fruit",
    "tiger": "National animal of India",
    "laptop": "Portable computer",
    "school": "A place where students learn"
}
score = 0
while True:
    word = random.choice(list(words.keys()))
    hint = words[word]
    guessed_letters = []
    wrong_attempts = 0
    max_attempts = 6
    print("\n" + "=" * 50)
    print("        HANGMAN GAME WITH HINTS")
    print("=" * 50)
    print("Hint:", hint)
    while wrong_attempts < max_attempts:
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print("\nWord:", display_word)
        if "_" not in display_word:
            print("\n🎉 Congratulations!")
            print("You guessed the word:", word)
            score += (max_attempts - wrong_attempts) * 10
            print("Current Score:", score)
            break
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed this letter.")
            continue
        guessed_letters.append(guess)
        if guess in word:
            print("✅ Correct!")
        else:
            wrong_attempts += 1
            print("❌ Wrong!")
            print("Remaining Attempts:", max_attempts - wrong_attempts)
    if wrong_attempts == max_attempts:
        print("\n💀 Game Over!")
        print("Correct Word:", word)
    print("\nFinal Score:", score)
    choice = input("\nDo you want to play again? (yes/no): ").lower()
    if choice != "yes":
        print("\nThank you for playing!")
        break