import sys
from stats import bookreport

def readfile(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        words = file_contents.split()
        lowered = file_contents.lower()
        chars = {}
        for i in range(0, len(lowered), 1):
            if lowered[i] in chars:
                chars[lowered[i]] += 1
            else:
                chars[lowered[i]] = 1
        bookreport(path_to_file, words, chars)

if __name__ == '__main__':
    sys.exit(readfile('books/frankenstein.txt'))