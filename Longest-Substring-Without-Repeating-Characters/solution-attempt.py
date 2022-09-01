#this is my attempt of the longest-substring-without-repeating-characters problem after looking at the solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = {}
        start = 0
        max = 0
        for j in range(0,len(s)):
            if s[j] in letters and letters[s[j]] >= start :
                start = letters[s[j]] +1
            letters[s[j]] = j
            max = (j+1-start) if max < (j+1-start) else max

        return max

s = "abcabcbb"
L = Solution()
a =L.lengthOfLongestSubstring(s)
print(a)
s = "bbbbb"
a=L.lengthOfLongestSubstring(s)
print(a)
s = "pwwkew"
a=L.lengthOfLongestSubstring(s)
print(a)

