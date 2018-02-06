#4_7_hangman_print_word
def print_word_with_blanks(word):
    display_word = ''
    for letter in word:
        if guessed_letters.find(letter) > -1:
            # letter found
            display_word = display_word + letter
        else:
            # letter not found
            display_word = display_word + '-'
    print display_word
