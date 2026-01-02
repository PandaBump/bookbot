import sys
from stats import *

def get_book_text(current_path_to_file):
    file_contents = ""
    with open(current_path_to_file) as f:
        file_contents = f.read()
    
    return file_contents
if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
current_path_to_file = sys.argv[1]


def main():
    
    file_contents = get_book_text(current_path_to_file)
    num_words = word_count(file_contents)
    char_freq = char_frequency(file_contents)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {current_path_to_file}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    print(sorted_char_count(char_freq))
    print("============= END ===============")
    

if __name__ == "__main__":
    main()