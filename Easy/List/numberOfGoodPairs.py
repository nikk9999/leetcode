# https://leetcode.com/problems/number-of-good-pairs/
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        goodPairs = [0] * 101
        totalGoodPairs=0
        for i in range(len(nums)):
            goodPairs[nums[i]]+=1
            totalGoodPairs+=(goodPairs[nums[i]]-1)
        return totalGoodPairs
        
            
                
            
