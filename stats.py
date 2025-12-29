# This function takes the content of a book as as string, 
# splits its content into words and returns the number of words
def count_words(book_string):
    words_list = book_string.split()
    return len(words_list)


def chars_count(book_as_string):
    character_dict = {}
    for ch in book_as_string:
        ch = ch.lower()
        if ch not in character_dict:
            character_dict[ch] = 1
        else:
            character_dict[ch] += 1
    return character_dict

def sort_on(list_of_dictionaries):
    return list_of_dictionaries["num"]


def chars_dict_to_sorted_list(dictionary_of_characters): 
    characters_list = []
    for i in dictionary_of_characters:
        if i.isalpha() != True:
            continue
        small_dict = {}
        small_dict["char"] = i
        small_dict["num"] = dictionary_of_characters[i]
        characters_list.append(small_dict)
    characters_list.sort(reverse=True, key=sort_on)
    return characters_list


    

"""sample_chars = {"a": 10, "b": 5, "c": 15}
result = sorted_characters(sample_chars)
print(result)"""


"""if __name__ == "__main__":
    text = "AAa aBb!!!"
    counts = count_characters(text)  # whatever you named your function
    print(counts)"""
    