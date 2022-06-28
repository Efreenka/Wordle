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


def letters_correct_wrong_position(guess, correct_word):
    word_length = len(correct_word)
    letters = []

    for i in range(word_length):
        if guess[i] in correct_word and guess[i] != correct_word[i]:
            letters.append(guess[i])
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
    print("Ahoj, vítej ve hře worlde by Efree ")
    all_words = preprocess.load_words("../data/game_words.txt")
    correct_word = random.choice(all_words)
    
    
    guess = ""
    while guess != correct_word:
        guess = input("Zadej slovo: ")
        
        if guess in all_words:
            wrong_letters = letters_wrong(guess, correct_word)
            print(f"Písmenka, která nejsou ve slově jsou: {wrong_letters} ")
            wrong_position = letters_correct_wrong_position(guess, correct_word)
            print(f"Písmenka, která jsou ve slově, ale na jiném místě jsou: {wrong_position} ")
            correct_letters = letters_correct_position(guess, correct_word)
            print(f"Písmenka, která jsou ve slově na správném místě jsou jsou: {correct_letters} ")
        else:
            print("Tohle slovo není ve slovníku, zkus to znovu!")
            
        if guess == correct_word:
            print("Gratuluju, tohle je správný tip!")


if __name__ == "__main__":
    wordle()



#testy:
#print(pismenka_nepatri("slovo", "heslo"))
#assert pismenka_nepatri("slovo", "heslo") == ["v"]
