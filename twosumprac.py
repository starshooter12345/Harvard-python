"""
class Solution:
    def findDivisiblePair(self,nums,k):
        #dictionary
        complements ={}

        for i in emumerate(nums):
            remainder = num % k

            if remainder in complements:
                return[complements[remainder],i]
            else:
                complements[(k-remainder) % k] = i
        return []
"""
class Solution:
    def findDivisiblePair(self, nums, k):
        complements = {}

        for i, num in enumerate(nums):
            remainder = num % k

            if remainder in complements:
                return [complements[remainder], i]
            else:
                complements[(k - remainder) % k] = i

        return []
