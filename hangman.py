#Create a number of guesses before player loses game
incorrect_guess_count = 5
#Create a word to compare guess with
hangman_word = "funpythonproject"
#Create a container for letters already guessed
guessed_letters = []
#Create an alphabet to prevent edge cases
alphabet = 'abcdefghijklmnopqrstuvwxyz'
while incorrect_guess_count > 0:

    user_guess = input("Choose a letter from a-z ").lower()

    if user_guess in hangman_word:
        print(f'"Congrats, {user_guess} is in the word!"')
        guessed_letters.append(user_guess)
    else:
        guessed_letters.append(user_guess)
        incorrect_guess_count = incorrect_guess_count - 1
        print(f'"Sorry, that letter is not in the hangman word, you have {incorrect_guess_count} number of guesses left "')

    #Create a counter to keep track of wrong guesses and when to end game
    countdown_of_doom = 0

    for letter in hangman_word:
        if letter in guessed_letters:
            print(letter, end= " ")
        else:
            print("_", end= " ")
            countdown_of_doom +=1
        
    if countdown_of_doom == 0:
        print(f"Wow, I can't believe you guessed the word {hangman_word} ! You are a genius ")
        break
else:
    print("Ouch, so close. Try the game again! <3 ")


        



