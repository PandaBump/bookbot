
def word_count(file_contents):
    words = file_contents.split()
    return len(words)

def char_frequency(file_contents):
    char_dict = {}
    for char in file_contents:
        if char.lower() in char_dict:
            char_dict[char.lower()] += 1
        else:
            char_dict[char.lower()] = 1
    return char_dict

def sort_on(items):
    return items["num"]

def sorted_char_count(char_dict):
    sorted_char_freq = sorted(char_dict.items(), key=lambda item: item[1], reverse=True)
    for char in sorted_char_freq:
        if char[0].isalpha() != True or char[0] == '' or char[0] == None:
            continue
        print(f"{char[0]}: {char[1]}")
    



