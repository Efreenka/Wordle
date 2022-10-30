import random
import preprocess


def letters_correct_position(guess, correct_word):
    word_length = len(correct_word)
    letters = []

    for i in range(word_length):
        if guess[i] == correct_word[i]:
            letters.append(guess[i])
        else:
            letters.append("_")

    return letters


def letters_correct_wrong_position(guess, correct_word, correct_letters):
    max_characters_counts = {}
    for letter in correct_word:
        max_characters_counts[letter] = correct_word.count(letter)

    letters = []
    for number in range(len(correct_word)):
        if guess[number] in correct_word and guess[number] != correct_word[number]:
            characters_count = correct_letters.count(guess[number])
            orange_characters_count = letters.count(guess[number])
            total = characters_count + orange_characters_count
            
            if total < max_characters_counts[guess[number]]:
                letters.append(guess[number])
            else:
                letters.append("_")
        else:
            letters.append("_")

    return letters


def letters_wrong(guess, correct_word):
    letters = []

    for letter in guess:
        if letter not in correct_word:
            letters.append(letter)

    return letters


def wordle():
    print("Ahoj, vítej ve hře worlde by Efree :)")
    all_words = preprocess.load_words("../data/game_words.txt")
    correct_word = random.choice(all_words)
    print(correct_word)
    
    guess = ""
    while guess != correct_word:
        guess = input("Zadej slovo: ")
        
        if guess in all_words:
            correct_letters = letters_correct_position(guess, correct_word)
            print(f"Písmenka, která jsou ve slově na správném místě jsou jsou: {correct_letters} ")
            wrong_position = letters_correct_wrong_position(guess, correct_word, correct_letters)
            print(f"Písmenka, která jsou ve slově, ale na jiném místě jsou: {wrong_position} ")
            wrong_letters = letters_wrong(guess, correct_word)
            print(f"Písmenka, která nejsou ve slově jsou: {wrong_letters} ")

        else:
            print("Tohle slovo není ve slovníku, zkus to znovu!")
            
        if guess == correct_word:
            print("Gratuluju, tohle je správný tip!")


if __name__ == "__main__":
    wordle()
