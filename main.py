from operator import itemgetter

def main(): 
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_words = get_word_count(text)
    char_dict = get_characters(text)
    sorted_chars = to_sorted_list(char_dict)
    print (f"--- Begin report of {book_path} ---")
    print (f"{num_words} words found in the book")
    print()

    for character in sorted_chars:
        print(f"The '{character['char']}' character was found '{character['num']}' times")

    print()

    print("--- End Report ---")

    
def get_word_count(text):
    word_list = text.split()
    return len(word_list)

def get_text(path):
    with open(path) as f:
        return f.read()
    
def get_characters(text):
    char_list = list(text.lower())      # Stores the text as a list of characters
    char_dict = {}
    for c in char_list:
        if c.isalpha():
            char_dict[c] = char_dict.get(c, 0) + 1              # Adds one to the key value for every character
    return char_dict

def to_sorted_list(character_dictionary):
    dict_list = []
    for c in character_dictionary:
        dict_list.append({"char" : c, "num" : character_dictionary[c]})
    sorted_list = sorted(dict_list, key=itemgetter("num"), reverse=True)
    return sorted_list

main()