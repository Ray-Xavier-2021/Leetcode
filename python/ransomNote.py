# Ransom Note
'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
'''
def canConstruct(ransomNote, magazine):
  """
  :type ransomNote: str
  :type magazine: str
  :rtype: bool
  """

  magArr = []

  mag = list(magazine)
  print('mag', mag)

  magLetters = magazine.split()

  counter = magLetters.count(mag)
  print('magLetters', magLetters)
  print('counter', counter)
  return counter


  
  


ransomNote1 = 'a'
magazine1 = 'b'

ransomNote2 = 'aa'
magazine2 = 'ab'

# ransomNote3 = 'Nice!'
# magazine3 = 'ine!'

ransomNote3 = 'aa'
magazine3 = 'aab'


ex1 = canConstruct(ransomNote1, magazine1)
ex2 = canConstruct(ransomNote2, magazine2)
ex3 = canConstruct(ransomNote3, magazine3)

print(ex1)
print(ex2)
print(ex3)