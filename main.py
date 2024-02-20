def get_book_text(text):
    with open(text) as f:
        return f.read()

def count_letters(text):
    letters_dict = {}
    for letter in text.lower():
        if letter not in letters_dict:
            letters_dict[letter] = 0
        else:
            letters_dict[letter] += 1
    return letters_dict

def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def sort_on(dict):
    return dict["num"]

def dict_to_sorted_list(dict):
    sorted_list = []
    
    for letter in dict:
        sorted_list.append({"char" : letter, "num": dict[letter]})
        
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_dict = count_letters(text)
    char_sorted_list = dict_to_sorted_list(char_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in char_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The {item['char']} character was found {item['num']} times")
    
    print("--- End Report ---")




main()