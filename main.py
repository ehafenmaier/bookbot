from stats import count_words, count_characters

def load_book_text(file_path):
    with open(file_path) as file:
        return file.read()
    
def main():
    book_file_path = "books/frankenstein.txt"
    book_text = load_book_text(book_file_path)
    word_count = count_words(book_text)
    character_counts = count_characters(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("-------- Character Count --------")
    for char in character_counts:
        print(f"'{char}': {character_counts[char]}")



if __name__ == "__main__":
    main()