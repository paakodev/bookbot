def sort_on(dict):
    return dict["count"]

def bookreport(path_to_file, words, chars):
    alphabet_count = []
    for k in chars:
        if k.isalpha():
            alphabet_count.append({"character": k, "count": chars[k]})
    alphabet_count.sort(reverse=True, key=sort_on)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}")
    print("----------- Word Count ----------")
    print(f"Found {len(words)} total words")
    print("--------- Character Count -------")
    for k in alphabet_count:
        char = k['character']
        count = k['count']
        print(f"{char}: {count}")
    print("============= END ===============")