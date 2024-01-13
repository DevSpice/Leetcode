'''
1347

You are given two strings of the same length s and t. In one step you 
can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

'''




class Solution:
    def minSteps(self, s: str, t: str) -> int:
        for x in s:
            t = t.replace(x, '',1)
        return len(t)

