def choose_vowels(letters):
    vowels = ['a', 'e', 'i', 'u', 'o']
    vowels_in_letters = filter(lambda x: x in vowels, letters)
    return list(vowels_in_letters)
