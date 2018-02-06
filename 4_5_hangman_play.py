#4_5_hangman_play

# This is a stub
def get_guess(word):
    return 'a'

# This is a stub
def process_guess(guess, word):
    global lives_remaining
    lives_remaining = lives_remaining - 1
    return False

def play():
    word = pick_a_word()
    while True:
        guess = get_guess(word)
        if process_guess(guess, word):
            print('You win! Well Done!')
            break
        if lives_remaining == 0:
            print('You are Hung!')
            print('The word was: ' + word)
            break
