class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_length = len(nums)
        sum_index = []

        for i in range(nums_length - 1):
            for j in range(i + 1,nums_length):
                if((nums[i] + nums[j]) == target):
                    sum_index.append(i)
                    sum_index.append(j)
                    return sum_index
        
        return sum_index