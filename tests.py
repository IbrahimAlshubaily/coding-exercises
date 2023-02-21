import unittest

import random
import string 
from anagrams import isAnagram

class Tests(unittest.TestCase):
    
    def test_anagrams(self):
        def create_random_anagram():
            chars = [random.choice(string.ascii_letters) for _ in range(int(random.random() * 100))]
            word = "".join(chars)
            random.shuffle(chars)
            other_word = "".join(chars)
            return word, other_word
        word, other_word = create_random_anagram()
        self.assertTrue(isAnagram(word, other_word))
        self.assertFalse(isAnagram(word, other_word[:-1]))


            


    
if __name__ == '__main__':
    unittest.main()