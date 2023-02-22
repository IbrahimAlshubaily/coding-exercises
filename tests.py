import unittest

import random
import string 
from anagrams import isAnagram
from binary_heap import BinaryHeap
from fib import fib

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

    def test_fib(self):
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(3), 2)

        self.assertEqual(fib(6), 8)
        self.assertEqual(fib(10), 55)
        self.assertEqual(fib(14), 377)
        self.assertEqual(fib(18), 2584)
        self.assertEqual(fib(1000), 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875)



            
if __name__ == '__main__':
    unittest.main()