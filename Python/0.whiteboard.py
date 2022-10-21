def containsDuplicate2(nums, k):
    unique = set()
    duplicateNum = None
    duplicateIndex = None
    for index, element in enumerate(nums):
        if element in unique:
            duplicateNum = element
            duplicateIndex = index
        else:
            unique.add(element)

    indexOfFirst = nums.index(duplicateNum)
    print(indexOfFirst)
    j = abs(indexOfFirst - duplicateIndex)
    print(j)

    return abs(indexOfFirst - duplicateIndex) <= k




print(containsDuplicate2([1, 0, 1, 1], 1)) #True
#print(containsDuplicate2([1, 2, 3, 1], 3)) #True