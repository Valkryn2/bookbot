from stats import get_book_text, sort_on
import sys

USER_INPUT = sys.argv


def main():
    if len(USER_INPUT) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    try:
        num_words, character_count, character_list = get_book_text(USER_INPUT[1])
    except Exception as e:
        print("are you sure you are using a correct address?", e)
        return None
    print(f'Found {num_words} total words')
    character_list.sort(reverse=True, key=sort_on)
    for char_data in character_list:
        print(f'{char_data["char"]}: {char_data["num"]} ')


if __name__ == "__main__":
    main()
