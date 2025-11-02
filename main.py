from stats import count_words, count_characters, sort_character_counts

def load_book_text(file_path):
    with open(file_path) as file:
        return file.read()
    
def main():
    book_file_path = "books/frankenstein.txt"
    book_text = load_book_text(book_file_path)
    word_count = count_words(book_text)
    character_counts = count_characters(book_text)
    sorted_character_counts = sort_character_counts(character_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("-------- Character Count --------")
    for char_count in sorted_character_counts:
        if char_count["char"].isalpha():
            print(f"{char_count["char"]}: {char_count["num"]}")



if __name__ == "__main__":
    main()