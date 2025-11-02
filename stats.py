
def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    character_counts = {}
    for char in text:
        char = char.lower()
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    return character_counts

def sort_on(items):
    return items["num"]

def sort_character_counts(character_counts):
    sorted_characters = []
    for char in character_counts:
        sorted_char = {"char": char, "num": character_counts[char]}
        sorted_characters.append(sorted_char)

    sorted_characters.sort(reverse=True, key=sort_on)
    return sorted_characters
