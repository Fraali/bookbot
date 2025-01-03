def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print_each_char(file_contents)
        return file_contents


def book_word_count(text):
    word_num = len(text.split())
    return word_num

def print_each_char(text):
    text = text.lower()
    allowed_characters = 'abcdefghijklmnopqrstuvwxyz'
    character_count = dict()
    for char in text:
        if char in allowed_characters:
            character_count.update({char : character_count.get(char, 0) + 1})
    sorted_char_count = list()

    for i in character_count:
        sorted_char_count.append([character_count[i], i])
    sorted_char_count.sort(reverse=True)

    for i in sorted_char_count:
        print(f"The '{i[1]}' character was found {i[0]} times")

    


main()