from turtle import left, right

class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxWindow = 0
        maxWindowLeft=0
        maxWindowRight=0
        answer = ""
        for i in range(0,len(s)):
            leftWindow = i
            rightWindow = i
            print("checking"+str(i))
            #checking odd palindromes
            while leftWindow >= 0 and rightWindow < len(s) and s[leftWindow] == s[rightWindow]:
                if rightWindow-leftWindow+1 > maxWindow:
                    maxWindow = rightWindow-leftWindow+1
                    maxWindowLeft= leftWindow
                    maxWindowRight= rightWindow

                leftWindow-=1
                rightWindow+=1
            #checking even palindromes
            leftWindow = i
            rightWindow = i +1
            while leftWindow >=0 and rightWindow < len(s) and s[leftWindow] == s[rightWindow]:
                if rightWindow-leftWindow+1 > maxWindow:
                    maxWindow = rightWindow-leftWindow+1
                    maxWindowLeft = leftWindow
                    maxWindowRight= rightWindow
                leftWindow-=1
                rightWindow+=1
        return s[maxWindowLeft:maxWindowRight+1:1]
mySolution= Solution()
print(mySolution.longestPalindrome("aacabdkacaa"))
print(mySolution.longestPalindrome("caba"))