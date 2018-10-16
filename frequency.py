"""Analyze the word frequencies in a book downloaded from Project Gutenberg."""

import string

def get_word_list(file_name):
    """Read the specified project Gutenberg book.

    Header comments, punctuation, and whitespace are stripped away. The function
    returns a list of the words used in the book as a list. All words are
    converted to lower case.
        -> process_file loops through the lines of the file, passing them to
    process_line
    """
    hist = {}
    fp = open(file_name)

    for line in fp:
        if line.startswith('ADVENTURE I. A SCANDAL IN BOHEMIA'):
            break

    for line in fp:
        line = line.replace('-', ' ') # replaces punctuation to space\
        for word in line.split():
            word = word.strip(string.punctuation + string.whitespace)
            word = word.lower()
            if len(word) >= 5:
                hist[word] = hist.get(word, 0) + 1
    print('hist', hist)
    return hist

def most_common(hist):
    """ Takes a histogram and returns a list of word-frequency tuples, sorted
        in reverse order by frequency-> decending"""
    t = []
    for key, value in hist.items():
        t.append((value, key))

    t.sort(reverse=True)
    return t

def get_top_n_words(hist, n):
    """Take a list of words as input and return a list of the n most
    frequently-occurring words ordered from most- to least-frequent.

    Parameters
    ----------
    word_list: [str]
        A list of words. These are assumed to all be in lower case, with no
        punctuation.
    n: int
        The number of words to return.

    Returns
    -------
    int
        The n most frequently occurring words ordered from most to least.
    frequently to least frequently occurring
    """

    t = most_common(hist)
    print 'The most common words are:'
    for freq, word in t[:n]:
        print word, '\t', freq

if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
    hist = get_word_list('sherlock.txt')
    #print(hist)
    get_top_n_words(hist, 10)
    #get_word_list('sherlock.txt')
