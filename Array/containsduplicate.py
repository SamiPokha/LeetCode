def containsduplicate(nums):
    h_set = set()
    for i, num in enumerate(nums):
        if num in h_set:
            return True
        h_set.add(num)
    return False

assert containsduplicate([1, 2, 3, 1]) == True
assert containsduplicate([1, 2, 3, 4]) == False
assert containsduplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
assert containsduplicate([1]) == False
assert containsduplicate([-1, -2, -3, -1]) == True
print("All 5 tests passed!")