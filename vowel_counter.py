def count_vowels(word: str) -> dict:
    vowels = ('a', 'e', 'i', 'o', 'u')
    diacritics = {
        'á': 'a',
        'é': 'e',
        'í': 'i',
        'ó': 'o',
        'ú': 'u',
        'ü': 'u',
        'Á': 'A',
        'É': 'E',
        'Í': 'I',
        'Ó': 'O',
        'Ú': 'U',
        'Ü': 'U'
    }
    clean_word = ''.join(diacritics.get(character, character).lower() for character in word if character.isalpha())
    result = {}
    for letter in clean_word:
        if letter in vowels:
            if letter not in result:
                result[letter] = 1
            else:
                result[letter] += 1
    result = {vowel: result.get(vowel, 0) for vowel in vowels}
    result = {vowel: count for vowel, count in result.items() if count != 0}
    return result