class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0 
        max_i = 0
        max_s = 0
        for i in range(0, len(nums)):
            if(nums[i] == 1):
                max_i = max_i + 1
            else:
                if(max_i != 0 and (max_i > max_s)):
                    max_s = max_i
                max_i = 0
        
        return max_i if (max_s <= max_i) else max_s
        
