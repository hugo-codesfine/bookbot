def count_words(book_string):
    splitted_book = book_string.split()
    book_word_count = len(splitted_book)
    return book_word_count


# ch = Key -> ch_counter = Value

def count_characters(book_as_string):
    character_dict = {}
    for ch in book_as_string:
        ch = ch.lower()
        if ch not in character_dict:
            character_dict[ch] = 1
        else:
            character_dict[ch] += 1
    return character_dict


"""if __name__ == "__main__":
    text = "AAa aBb!!!"
    counts = count_characters(text)  # whatever you named your function
    print(counts)"""
    