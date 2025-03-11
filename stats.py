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
