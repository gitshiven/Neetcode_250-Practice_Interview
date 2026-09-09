class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return None
        left, right = 0, len(numbers)-1
        sum = 0
        while left<right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left+1, right+1]
            elif sum<target:
                left+=1
            else:
                right-=1