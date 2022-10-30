from wordle import letters_correct_position, letters_correct_wrong_position, letters_wrong

assert letters_correct_position("kokos", "kočka") == ["k", "o", "_", "_", "_"]
assert letters_correct_position("kočka", "kočka") == ["k", "o", "č", "k", "a"]
assert letters_correct_position("myčka", "strup") == ["_", "_", "_", "_", "_"]

assert letters_correct_wrong_position("kokos", "kočka", ["k", "o", "_", "_", "_"]) == ["_", "_", "k", "_", "_"]
assert letters_correct_wrong_position("kočka", "kočka", ["k", "o", "č", "k", "a"]) == ["_", "_", "_", "_", "_"]
assert letters_correct_wrong_position("myčka", "strup", ["_", "_", "_", "_", "_"]) == ["_", "_", "_", "_", "_"]
assert letters_correct_wrong_position("edcba", "abcde", ["_", "_", "c", "_", "_"]) == ["e", "d", "_", "b", "a"]

assert letters_wrong("kokos", "kočka") == ["s"]
assert letters_wrong("kočka", "kočka") == []
assert letters_wrong("myčka", "strup") == ["m", "y", "č", "k", "a"]
