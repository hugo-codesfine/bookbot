
def get_book_text(path_to_file):
    with open(path_to_file, encoding="utf-8") as f:
        book_contents = f.read()
    return book_contents

def main():
    print(get_book_text("books/frankenstein.txt"))

main()