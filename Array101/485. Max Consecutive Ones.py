def findMaxConsecutiveOnes(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_counter = 0
    temp_counter = 0
    if len(nums) == 1 and nums[0] == 1:
        return 1

    for index in range(len(nums)):
        if nums[index] == 1:
            temp_counter += 1
        else:
            if temp_counter > max_counter:
                maxccccccc_counter = temp_counter
            temp_counter = 0
    if temp_counter > max_counter:
        max_counter = temp_counter
    return max_counter


if __name__ == '__main__':
    nums = [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1]
    print(findMaxConsecutiveOnes(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
