# this is my attempt (brute force)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        #make a iterator
        a = list(range(0,len(nums)))
        # iterate through elements of the nums starting at 0th element
        for x in a:
            # only iterate if x is smaller then target 
            #if x <= target:
            #Turns out this won't work with negative numbers.
                # iterate through elements of the nums starting at nth element
                for y in a[::-1]:
                    # only iterate until xth element
                    if y > x:
                        if (nums[x]+nums[y] == target):
                            return [x,y] 
s = Solution()
print(s.twoSum([2,7,11,5], 9))
print(s.twoSum([-1,-2,-3,-4,-5], -8))
print(s.twoSum([3,2,4], 6))
print(s.twoSum([3,3],6))
