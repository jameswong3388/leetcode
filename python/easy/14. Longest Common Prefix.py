def longestCommonPrefix(strs):
    if not strs:
        return ""

    length = len(strs[0])
    count = len(strs)
    for i in range(length):  # iterate through the first string
        c = strs[0][i]
        for j in range(1, count):
            # compare the character with the same index in other strings
            if len(strs[j]) == i or strs[j][i] != c:
                return strs[0][:i]

    return strs[0]


print(longestCommonPrefix(["flower", "flow", "flight"]))
