STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]
# file = one-today.txt
# define the file that the program will be reading
# this line not necessary. 
# for reference tried "python3 word_frequency.py one-today.txt" compared to "python3 word_frequency.py praise_song_for_the_day.txt"
# this is when concept began to sink in and applied to terminal to check each function


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    file = open(file)
    text = file.read()
    # print(text)
    # verified text from one-today prints in terminal using python3 word_frequency.py one-today.txt
    
    
    text_formatting = text.lower().replace('.','').replace(',','').replace('!','').replace('?','').replace('—','').replace(':','').split()
    # print(text_formatting)
    # this function works for every symbol except for '-'
    # fixed by copying the actual '-' from the text file. length of '-' is longer than usual keyboard hyphen.

    word_count = []

    for word in text_formatting:
        if word not in STOP_WORDS:
            word_count.append(word)
            # print(word_count)
    # this function removes stop words defined at top of file.
    # originally had every function in text_formatting in a new line. 
    # this appeared to work until adding word count, which printed each individual letter. revised text formatting above.

    x = {}
    for word in word_count:
        if word not in x.keys():
            x[word] = 1
        else:
            x[word] += 1
            # print(x)

    sort_text = sorted(x, key=x.get, reverse=True )
    for num in sort_text:
        print(num, x[num], '*' * x[num])

    # fixed asterisk by mulitplying '*' by the value of number used

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
