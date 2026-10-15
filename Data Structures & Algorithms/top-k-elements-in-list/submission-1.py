class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter={}
        
        seen=set(nums)
        for num in nums:
            counter[num]=counter.get(num,0)+1
        counter=dict(sorted(counter.items(),key= lambda x:x[1],reverse=True))

        return list(counter.keys())[:k]
        
        

