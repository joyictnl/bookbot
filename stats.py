def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    # convert to lowercase
    text = text.lower()
    # return a dictionary of string -> int
    # where the key is the character and the value is the number of times it appears   
    # in the text
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

