
def hangman(word):
    wrong_guesses = 0
    stages = ["", "________      ", "|      |      ",
              "|      0      ", "|     /|\     ", "|     / \     ", "|"]
    remaining_letters = list(word)
    letter_board = ["*"] * len(word)
    win = False
    print('Welcome to Hangman')
    while wrong_guesses < len(stages)-1:
        print('\n')
        guess = input("Guess a letter: ")
        if guess in remaining_letters:
            character_index = remaining_letters.index(guess)
            letter_board[character_index] = guess
            remaining_letters[character_index] = '&'
        else:
            wrong_guesses += 1
        print((''.join(letter_board)))
        print('\n'.join(stages[0: wrong_guesses + 1]))
        if '*' not in letter_board:
            print('You win! The word was : {}'.format(word))
            win = True
            break
    if win == False:
        print('\n'.join(stages[0: wrong_guesses]))
        print('You lose! The words was {}'.format(word))


hangman("cat")
