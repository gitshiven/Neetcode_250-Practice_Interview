class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_array = [1] * len(nums)
        right_array = [1] * len(nums)

        for i in range(1, len(nums)):
            left_array[i] = left_array[i-1] * nums[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            right_array[i] = right_array[i+1] * nums[i+1]
        
        output = []
        for i in range(len(nums)):
            output.append(left_array[i]*right_array[i])
        return output
            
            
            