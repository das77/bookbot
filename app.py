def get_book(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def count_words(book):
    words = book.split()
    return len(words)

def count_characters(book):
    # Convert all uppercase letters to lowercase
    text = book.lower()
    # Initialize a dictionary to store character counts
    char_counts = {}
    # Iterate through each character in the text
    for char in text:
        # Check if the character is alphanumeric
        if char.isalpha():
            # Increment the count for this character in the dictionary
            char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

def dict_to_list_of_dicts(dictionary):
    list_of_dicts = []
    for key, value in dictionary.items():
        list_of_dicts.append({key: value})
    return list_of_dicts

def sort_on(dict):
    dict.sort(key=lambda x: list(x.values())[0], reverse=True)

def gen_report(book, words, chars):
    report = f'--- Begin report of {book} ---\n'
    report += f"{words} words found in the document\n"
    for x in chars:
        for key, value in x.items():
            report += f'The {key} character was found {value} times\n'
    report += '--- End Report ---'
    return report


def main():
    book_loc = '/home/dspera/Projects/bookbot/books/frankenstein.txt'
    book_text = get_book(book_loc)
    num_words = count_words(book_text)
    num_chars = count_characters(book_text)
    char_list = dict_to_list_of_dicts(num_chars)
    sort_on(char_list)
    rep = gen_report(book_loc, num_words, char_list)
    print(rep)

if __name__ == '__main__':
    main()