from stats import count_words, count_characters, sorted_characters


def get_book_text(path_to_file):
    with open(path_to_file, encoding="utf-8") as f:
        book_contents = f.read()
    return book_contents

        

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_text)
    num_characters = count_characters(book_text)
    sorted_list = sorted_characters(num_characters)
    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_list:
        print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")
    #print(sorted_list['char'])
    #print(get_book_text("books/frankenstein.txt"))

main()