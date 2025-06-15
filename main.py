from stats import get_book_text


def main():
    num_words, character_count = get_book_text("books/frankenstein")
    print(f'{num_words} words found in the document')
    print(character_count)


if __name__ == "__main__":
    main()
