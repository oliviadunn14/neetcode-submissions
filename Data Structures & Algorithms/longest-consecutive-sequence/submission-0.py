class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        sorted_nums=sorted(nums)
        current_length=1
        max_length=1

        for i in range(1,len(sorted_nums)):
            if sorted_nums[i]==sorted_nums[i-1]+1:
                current_length+=1
            elif sorted_nums[i]==sorted_nums[i-1]:
                continue
            else:
                current_length=1
            
            max_length=max(max_length,current_length)
        
        return max_length

    
        



