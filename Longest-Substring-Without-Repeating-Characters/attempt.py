class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #print(s)
        start = 0
        end = 0
        curr = 0
        max = 0
        letters = {}
        for x in s:
            #print("currently looking at " + x+" located at "+str(curr))
            if x not in letters:
                letters[x] = curr
                max = (end+1-start) if (end+1 - start > max) else max
                #print("added to dictionary, dictionary looks like following : " +str(letters))
               
            elif x in letters:
                #print(x+" in dict at"+ str(letters[x]))
                #print(letters)
                #print("popping from "+str(start)+ " to "+str(letters[x]))
                
                for i in range(start,letters[x]+1):
                    #print("popping loop i is :"+str(i))
                    if s[i] in letters and letters[s[i]] < letters[x]: 
                        #print("popped " +s[i])
                        letters.pop(s[i])
                start = letters[x]+1
                #print("final popoed:"+x)
                letters.pop(x)
                letters[x] = curr
                #print(letters)
            
            #print("end is: "+ str(end) + " and start is : " + str(start))
            curr +=1
            end +=1
        #print(letters)
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