"""
Write a class called WordPlay. It should have a constructor that holds a list of words. The user of the class should pass the 
list of words through constructor, which user wants to use for the class. The class should have following methods:
	words_with_length(length) — returns a list of all the words of length length
	starts_with(char1) — returns a list of all the words that start with char1
	ends_with(char2) — returns a list of all the words that end with char2
	palindromes() — returns a list of all the palindromes in the list
	only(str1) — returns a list of the words that contain only those letters in str1
	avoids(str2) — returns a list of the words that contain none of the letters in str2
Make Required object for WordPlay class and test all the methods.
For Example:
If input list entered by user is: ['apple', 'banana', 'find', 'dictionary', 'set', 'tuple', 'list', 'malayalam', 'nayan', 'grind', 'apricot']
words_with_length (5) should return ['apple', 'tuple', 'nayan', 'grind']
starts_with ('a') should return ['apple', 'apricot']
ends_with ('d') should return ['find', 'grind']
palindromes () should return ['malayalam', 'nayan']
only ('bna') should return ['banana']
avoids ('amkd') should return ['set', 'tuple', 'list']
"""

class WordPlay:
    def __init__(self,words: list[str]):
        self.words = words

    def words_with_length(self,length):
        return list(filter(lambda x: len(x) == length, self.words))
    
    def starts_with(self,prefix):
        return list(filter(lambda x: x.startswith(prefix), self.words))
    
    def ends_with(self,suffix):
        return list(filter(lambda x: x.endswith(suffix), self.words))
    
    def palindromes(self):
        return list(filter(lambda x: x == x[::-1], self.words))
    
    def only(self, chars):
        return list(filter(lambda x: all([c in x for c in chars]), self.words))
    
    def avoids(self, chars):
        return list(filter(lambda x: all([c not in x for c in chars]), self.words))
    
words = ['apple', 'banana', 'find', 'dictionary', 'set', 'tuple', 'list', 'malayalam', 'nayan', 'grind', 'apricot']
wp = WordPlay(words)
print(wp.words_with_length(5))
print(wp.starts_with('a'))
print(wp.ends_with('d'))
print(wp.palindromes())
print(wp.only('bna'))
print(wp.avoids('amkd'))

"""
Output:
['apple', 'tuple', 'nayan', 'grind']
['apple', 'apricot']
['find', 'grind']
['malayalam', 'nayan']
['banana']
['set', 'tuple', 'list']
"""