def load_book_text(file_path):
    with open(file_path) as file:
        return file.read()

def count_words(text):
    words = text.split()
    return len(words)
    
def main():
    book_text = load_book_text("./books/frankenstein.txt")
    word_count = count_words(book_text)
    print(f'Found {word_count} total words')



if __name__ == "__main__":
    main()