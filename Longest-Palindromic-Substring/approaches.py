class SolutionDynamicProgramming:
    #LONGEST COMMONT SUBSTRING WITH ITSELF USING A REVERSE
    def longestPalindrome(self, s: str) -> str:
        reverseS = s[::-1]
        max = 0 
        maxI = 0
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        for i in range(0,len(s)):
            for j in range(0,len(s)):
                if reverseS[j] == s[i]:
                    if i == 0 or j ==0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j-1] +1
                if max < dp[i][j]: 
                    max = dp[i][j] 
                    maxI = i
        print("maxi is : "+str(maxI))
        print("max is : " + str(max))
        if max == 0:
            return s[0]
        else:
            for i in range(0,len(s)):
                
                print(dp[i]) 
            return s[maxI+1 - max: maxI+1:1]
mySolution= SolutionDynamicProgramming()
print(mySolution.longestPalindrome("aacabdkacaa"))
print(mySolution.longestPalindrome("caba"))
                    