def load_book_text(file_path):
    with open(file_path) as file:
        return file.read()
    
def main():
    book_text = load_book_text("./books/frankenstein.txt")
    print(book_text)


main()
