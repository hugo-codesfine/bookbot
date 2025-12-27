import sys
from stats import count_words, count_characters, sorted_characters

print(sys.argv)


def get_book_text(path_to_file):
    with open(path_to_file, encoding="utf-8") as f:
        book_contents = f.read()
    return book_contents

        

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    num_characters = count_characters(book_text)
    sorted_list = sorted_characters(num_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}\n----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_list:
        print(f"{i['char']}: {i['num']}")
    print("============= END ===============")

main()