#this is my attempt of the two sum problem after looking at the solution.
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        #dictionary
        hashmap = {}
        for x in range(0,len(nums)):
            real_target = target - nums[x]
            if real_target in hashmap:
                return [x, hashmap[real_target]]
            elif nums[x] not in hashmap:
                hashmap[nums[x]] = x 
            