# two words are anagarms if one can formed by re arranging characters of the other.
def isAnagram(word: str, other_word: str) -> bool:
    if len(word) != len(other_word):
        return False
    
    word_count = {}
    for ch in word:
        if ch not in word_count:
            word_count[ch] = 0
        word_count[ch] += 1
    
    for ch in other_word:
        if ch not in word_count or word_count[ch] <= 0:
            return False
        word_count[ch] -= 1
    return True