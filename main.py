from stats import count_words


def get_book_text(path_to_file):
    with open(path_to_file, encoding="utf-8") as f:
        book_contents = f.read()
    return book_contents

        

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")
    #print(get_book_text("books/frankenstein.txt"))

main()