def groupanagram(strs):
    if len(strs) == 0:
        return []

    hash_map = {}

    for string in strs:
        count = [0] * 26
        for i in range(len(string)):
            count[ord(string[i]) - ord('a')] += 1

        key = tuple(count)
        if key not in hash_map:
            hash_map[key] = []
        hash_map[key].append(string)

    return list(hash_map.values())

norm = lambda res: sorted([sorted(group) for group in res])

assert norm(groupanagram(["eat","tea","tan","ate","nat","bat"])) == norm([["bat"],["nat","tan"],["ate","eat","tea"]])
assert norm(groupanagram([""])) == norm([[""]])
assert norm(groupanagram(["a"])) == norm([["a"]])
assert norm(groupanagram(["abc", "bca", "cab"])) == norm([["abc", "bca", "cab"]])
assert norm(groupanagram(["bdddddddddd", "bbbbbbbbbbc"])) == norm([["bdddddddddd"], ["bbbbbbbbbbc"]])
print("All 5 tests passed!")