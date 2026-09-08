class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countNums = {}
        for i in range(len(nums)):
            countNums[nums[i]] = 1 + countNums.get(nums[i],0)
        
        sorted_countNums = sorted(countNums, key = countNums.get, reverse=True)
        
        return sorted_countNums[:k]


