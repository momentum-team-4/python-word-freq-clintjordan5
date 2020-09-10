STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]
file = one-today.txt
# define the file that the program will be reading


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    file = open(file)
    text = file.read()
# file is the one-today.txt used

    removePunctuation = ""
    letter = [abcdefghijklmnopqrstuvwxyz]
    # unsure if most efficient method here
    for letter in text:
        if letter not in list.removePunctuation:
            removePunctuation = removePunctuation + letter
            print(removePunctuation)
            # attempting to define a list of valid letters A-Z, if a character is not in the list, remove it

    lowercase = removePunctuation.lower()
    split = lowercase.split()
    print(split)
    # using lower and split functions

    # what to use here to begin loop?
    for text in file
    text.replace('.', '')
    text.replace('!', '')
    text.replace('?', '')
    text.replace(':', '')
    # this is a placeholder, want to make a for loop and replace symbols/punctuation with empty string
    # for my own reference, I'll often do a few lines or functions at a time and test them, then edit accordingly
    # as in Javascript look at console.log
    # HTML/CSS classes and ID make bright colors and formatting for each to see what works.
    # Looking for a similar comparison in Python to edit code.

    # output =[{text in split if not text in STOP_WORDS:]
    # above line commented out, would that function do the same as below?

    def output = []
    for text in output
    if text not in STOP_WORDS:
        output.append(word)
        print output
    # if the text is not in the stop words list, add that word to the output

    frequency = {}
    for word in output:
        frequency[word] = frequency.get(word, 0) + 1
        return frequency
    # get the frequency of words used in text file, referencing the above output function on 28

    def word_count(str):
        count = dict()
        words = str.split()

    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    return count
    # word count function works in theory, unsure of where to place it in code


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
