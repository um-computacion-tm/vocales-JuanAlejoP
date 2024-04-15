import unittest
from vowel_counter import count_vowels

class TestVocalCounter(unittest.TestCase):
    def test_nothing(self):
        word = ''
        result = count_vowels(word)
        self.assertEqual(result, {})
    
    def test_noVowels_1(self):
        word = 'tryhgf'
        result = count_vowels(word)
        self.assertEqual(result, {})

    def test_noVowels_2(self):
        word = 'sdfghjklñ'
        result = count_vowels(word)
        self.assertEqual(result, {})

    def test_1Vowel_o(self):
        word = 'sol'
        result = count_vowels(word)
        self.assertEqual(result, {'o': 1})

    def test_2Vowels_o(self):
        word = 'solo'
        result = count_vowels(word)
        self.assertEqual(result, {'o': 2})

    def test_2Vowels_different(self):
        word = 'sola'
        result = count_vowels(word)
        self.assertEqual(result, {'a': 1, 'o': 1})

    def test_everyVowel(self):
        word = 'murciélago'
        result = count_vowels(word)
        self.assertEqual(result, {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1})

    def test_onlyVowels(self):
        word = 'aeioiuuioea'
        result = count_vowels(word)
        self.assertEqual(result, {'a': 2, 'e': 2, 'i': 3, 'o': 2, 'u': 2})

    def test_email(self):
        word = 'j.patino@alumno.um.edu.ar'
        result = count_vowels(word)
        self.assertEqual(result, {'a': 3, 'e': 1, 'i': 1, 'o': 2, 'u': 3})

    def test_longWord(self):
        word = 'Parangaricutirimícuaro'
        result = count_vowels(word)
        self.assertEqual(result, {'a': 4, 'i': 4, 'o': 1, 'u': 2})

    def test_dinosaur(self):
        word = 'Giganotosaurus carolinii'
        result = count_vowels(word)
        self.assertEqual(result, {'a': 3, 'i': 4, 'o': 3, 'u': 2})

    def test_pingüino(self):
        word = 'los pingüinos jamás volarán'
        result = count_vowels(word)
        self.assertEqual(result, {'a': 4, 'i': 2, 'o': 3, 'u': 1})

    def test_upperVowels(self):
        word = 'MuRcIÉlagO'
        result = count_vowels(word)
        self.assertEqual(result, {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1})

    def test_phrase1(self):
        expected = {
            'a': 5,
            'e': 1,
            'u': 1,
        }
        result = count_vowels('acá hay una frase')
        self.assertDictEqual(result, expected)

    def test_phrase2(self):
        word = 'sOlaMenTE qUiERo que gAne bOcA'
        result = count_vowels(word)
        self.assertEqual(result, {'a': 3, 'e': 5, 'i': 1, 'o': 3, 'u': 2})

    def test_phrase3(self):
        expected = {
            'a': 2,
            'e': 2,
            'o': 2,
        }
        result = count_vowels('vamos de paseo')
        self.assertDictEqual(result, expected)

unittest.main()