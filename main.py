from sys import argv, exit
from os import path
from stats import get_num_words
from stats import get_num_characters

def main(book_path):
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    # Get the word count
    print(f"Found {num_words} total words")
    
    print("----------- Character Count -----")
    # Get the character counts
    char_counts = get_num_characters(text)

    # Sort the characters by count in descending order
    sorted_chars = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)
    for char, count in sorted_chars:
        if char.isalpha():  # Only print alphabetic characters
            print(f"{char}: {count}")

    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    
    book_path = argv[1]
    main(book_path)
