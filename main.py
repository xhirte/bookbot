def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    counted_words = count_words(text)
    counted_letters  = count_letters(text)
    flattened_list = flatten_list(counted_letters)
    print(f"{counted_words} words found in the document")
    for entry in flattened_list:
        print(f"The {entry["name"]} character was found {entry['num']} times")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(words):
    splitted_string = words.split()
    return len(splitted_string)

def count_letters(text):
    dictonary_counted_letters = {}
    lowered_string = text.lower()
    for letter in lowered_string:
        if letter in dictonary_counted_letters:
            dictonary_counted_letters[letter] += 1
        else: dictonary_counted_letters[letter] = 1

    return dictonary_counted_letters



def flatten_list(raw_data):
    flattened_list = []
    for key, value in raw_data.items():
        if key.isalpha():
            temp = {"name": key,"num": value}
            flattened_list.append(temp)
    
    flattened_list.sort(reverse=True, key=sort_on)

    return flattened_list
    
    
def sort_on(dict):
    return dict["num"]

main()
