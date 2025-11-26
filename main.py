from stats import count_words
from stats import count_characters
from stats import count_characters, chars_dict_to_sorted_list
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    
    book_text = get_book_text(book_path)

    num_words = count_words(book_text)
    char_counts = count_characters(book_text)
    sorted_chars = chars_dict_to_sorted_list(char_counts)

    print("============ BOOKBOT ============")
    print()
    print(f"Analyzing book found at {book_path}...")
    print()
    print("----------- Word Count ----------")
    print()
    print(f"Found {num_words} total words")
    print()
    print("--------- Character Count -------")
    print()
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print()
    print("============= END ===============")

main()