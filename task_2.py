import random

def hangman() :

    words = ['Apple', 'Banana', 'Orange', 'Mango', 'Grapes', 'Peach']
    word = random.choice(words).lower()
    guessed = ['_'] * len(word)
    attempts = 5
    guessed_letters = []

    print("Welcome to Hangman !")
    print("Guess The word , One letter At a Time. ")
    print("You have only 3 Worng Guesses Allowed.")

    while attempts > 0 and ''.join(guessed) != word:

        print(''.join(guessed))
        print("Guessed Letter : ", ','.join(guessed_letters) if guessed_letters else 'none')
        print("Remaining Attemps : ", attempts)
        guess = input("Enter a Letter :").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please Enter a valid letter")
            continue

        if guess in guessed_letters:
            print("This Guess is already done. Try another.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good Guess ! ", guess, "Is inthe word")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
        else:
            print("Wrong guess", guess, "is not in the word")
            attempts -= 1

    if ''.join(guessed) == word:
        print("Congrats! Youe've guessed the word : ", word)
    else:
        print("Game over! The Word was :", word)


if __name__ == "__main__" :
    hangman()








