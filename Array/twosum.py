def twoSum(nums, target):
    h_map = {}
    for i, num in enumerate(nums):
        value = target - num
        if value in h_map:
            return [h_map[value], i]
        h_map[num] = i
    return None

assert sorted(twoSum([2, 7, 11, 15], 9)) == [0, 1]
assert sorted(twoSum([3, 2, 4], 6)) == [1, 2]
assert sorted(twoSum([3, 3], 6)) == [0, 1]
assert sorted(twoSum([-3, 4, 3, 90], 0)) == [0, 2]
assert sorted(twoSum([0, 4, 3, 0], 0)) == [0, 3]
print("All 5 tests passed!")