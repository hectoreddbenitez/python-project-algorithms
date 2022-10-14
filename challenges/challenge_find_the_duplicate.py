def find_duplicate(nums):
    nums.sort()
    for index in range(0, len(nums) -1):
        if type(nums[index]) == str or nums[index] < 0:
                return False

        if nums[index] == nums[index + 1]:
                return nums[index]

    return False
print(find_duplicate([2, 3, 1, 5, 5, 6, 8, 9]))