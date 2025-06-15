def get_stats(lst):
    book_characters = {}
    for words in lst:
        for char in words.lower():
            if char not in book_characters:
                book_characters[char] = 1
            else:
                book_characters[char] += 1
    return book_characters


def get_book_text(file_path: str) -> int:
    with open(file_path, "r") as file:
        file_content = file.read()
        list_words = file_content.split()
        characters_dict = get_stats(list_words)
        word_count = len(list_words)
    return word_count , characters_dict
