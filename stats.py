def get_stats(lst):
    book_characters = {}
    for words in lst:
        for char in words.lower():
            if char not in book_characters:
                book_characters[char] = 1
            else:
                book_characters[char] += 1
    char_list = []
    for char, count in book_characters.items():
        char_list.append({"char": char, "num": count})

    return book_characters, char_list


def get_book_text(file_path: str) -> int:
    with open(file_path, "r") as file:
        file_content = file.read()
        list_words = file_content.split()
        characters_dict, character_list = get_stats(list_words)
        word_count = len(list_words)
    return word_count, characters_dict, character_list

def sort_on(dct):
    return dct["num"]