import sys

def sort_on(dict):
    return dict["count"]

def bookreport(path_to_file, words, chars):
    alphabet_count = []
    for k in chars:
        if k.isalpha():
            alphabet_count.append({"character": k, "count": chars[k]})
    alphabet_count.sort(reverse=True, key=sort_on)
    
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{len(words)} words was found in the document")
    print()
    for k in alphabet_count:
        char = k['character']
        count = k['count']
        print(f"The '{char}' character was found {count} times.")
    print("--- End report ---")

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