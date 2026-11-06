def containsduplicateII(nums, k):
    h_set = set()
    for i, num in enumerate(nums):
        if num in h_set:
            return True
        h_set.add(num)
        if len(h_set) > k:
            h_set.remove(nums[i - k])
    return False

assert containsduplicateII([1, 2, 3, 1], 3) == True
assert containsduplicateII([1, 0, 1, 1], 1) == True
assert containsduplicateII([1, 2, 3, 1, 2, 3], 2) == False
assert containsduplicateII([99, 99], 2) == True
assert containsduplicateII([1, 2, 1], 0) == False
print("All 5 tests passed!")