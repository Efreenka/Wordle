def load_words(filename):
    with open(filename, mode="r", encoding='utf-8') as file: 
        lines = file.readlines()
        processed_words = []

        for line in lines:
            processed_word = line.rstrip()
            processed_words.append(processed_word)

        return processed_words


def filter_words_with_length(words, length):
    correct_words = []
    for word in words:
        if len(word) == length:
            correct_words.append(word.lower())

    return correct_words


def write_words_to_file(words, filename):
    with open(filename, mode="w", encoding='utf-8') as file: 
        for word in words:
            print(word, file=file)             
       

if __name__ == "__main__":
    words = load_words("../data/czech_nouns.txt")
    words_filtered = filter_words_with_length(words, 5)
    write_words_to_file(words_filtered, "../data/game_words.txt")
