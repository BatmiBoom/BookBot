import sys
import os

from stats import get_chars_count, get_sorted_char_count, get_words_total_count

def get_book_text(file_path: str) -> str:
    if not os.path.exists(file_path):
        raise Exception("The File Doesnt Exist")

    with open(file_path) as f:
        contents = f.read()
        return contents

def main():
    args = sys.argv
    if len(args) < 2 or len(args) > 2:
        print("ERROR: wrong number of arguments")
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = args[1]
    
    try:
        contents = get_book_text(file_path)
    except Exception as e:
        print("ERROR: ", e)
        sys.exit(1)

    word_count = get_words_total_count(contents)
    char_count = get_chars_count(contents)
    sorted_char_count = get_sorted_char_count(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for pair in sorted_char_count:
        if type(pair["char"]) is str and pair["char"].isalpha():
            print(f"{pair["char"]}: {pair["num"]}")

    print("============= END ===============")

    
if __name__ == "__main__":
    main()
