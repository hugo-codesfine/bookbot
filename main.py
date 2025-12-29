import sys
from stats import count_words, chars_count, chars_dict_to_sorted_list

# This function returns a book content as a string from a provided path
def get_book_text(path_to_book):
    with open(path_to_book, encoding="utf-8") as f:
        return f.read()

        

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    num_characters = chars_count(book_text)
    sorted_list = chars_dict_to_sorted_list(num_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}\n----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_list:
        print(f"{i['char']}: {i['num']}")
    print("============= END ===============")

main()