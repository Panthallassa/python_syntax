words = ['wonder', 'glory', 'pride', 'tardiness', 'effervescent']


def print_words_starting_with_letters(words, letters):
    '''prints words that start with the inputed letter/s'''

    for word in words:
        if word[0].lower() in letters:
            print(word)

