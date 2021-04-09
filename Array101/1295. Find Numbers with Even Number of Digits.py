"""
author: Nabiha Raza
"""
class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even_count = 0
        digit_count = 0

        nums = list(str(nums))
        for index in range(len(nums[:-1])):
            if nums[index] == '[' or nums[index] == ']' or nums[index] == ' ':
                continue
            else:
                if ord(nums[index]) <= 57 and ord(nums[index]) >= 48:
                    digit_count += 1
                else:
                    if digit_count % 2 == 0:
                        even_count += 1
                    digit_count = 0
        if digit_count % 2 == 0:
            even_count += 1
        return even_count
