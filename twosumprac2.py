class Solution:
    def threeSum(self, nums, target): #k is the target
        complements = {}

        for i, num in enumerate(nums):
            if num in complements:
                return [complements[num], i]
            else:
                complements[target - num] = i
    
    
        for j, num in enumerate(nums):
            if num in complements:
                return [complements[num], j]
            else:
                complements[target - num] = i
        return []

    