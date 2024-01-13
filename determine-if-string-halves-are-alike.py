'''

1704 - Easy

You are given a string s of even length. Split this string into two halves 
of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels 
('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). 
Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.


'''

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = "aeiouAEIOU"
        s1 = 0
        s2 = 0
        length = int (len(s)/2)
        for x in range(length):
            if s[x] in vowels:
                s1 += 1
        for x in range(length, len(s)):
            if s[x] in vowels:
                s2 += 1

        return s1 == s2
