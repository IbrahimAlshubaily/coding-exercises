import unittest

import random
import string 
from anagrams import isAnagram
from binary_heap import BinaryHeap

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

    
    def test_binary_heap(self):
        heap = BinaryHeap()
        self.assertEqual(len(heap), 0)
        
        heap.insert(1)
        self.assertEqual(len(heap), 1)
        self.assertEqual(heap.peak(), 1)
        
        heap.insert(2)
        self.assertEqual(len(heap), 2)
        self.assertEqual(heap.peak(), 1)

        heap.insert(-1)
        self.assertEqual(len(heap), 3)
        self.assertEqual(heap.peak(), -1)

        self.assertEqual(heap.remove(), -1)
        self.assertEqual(len(heap), 2)

        self.assertEqual(heap.peak(), 1)
        self.assertEqual(heap.remove(), 1)
        self.assertEqual(len(heap), 1)

        self.assertEqual(heap.peak(), 2)
        self.assertEqual(heap.remove(), 2)
        self.assertEqual(len(heap), 0)

        self.assertEqual(heap.peak(), None)
        self.assertEqual(heap.remove(), None)

            
if __name__ == '__main__':
    unittest.main()