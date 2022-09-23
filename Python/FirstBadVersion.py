# https://leetcode.com/problems/first-bad-version/


bad = 0
def isBadVersion(version: int) -> bool:
    if version >= bad:
        return True
    return False

def firstBadVersion(n: int) -> int:
    if n < 2:
        return 1
    
    left = 1
    right = n
    while (left <= right): 
        mid = (left + right) // 2
        if isBadVersion(mid) == True and isBadVersion(mid-1) == False:
            return mid 
        elif isBadVersion(mid-1) == True: 
            right = mid -1
        else: 
            left = mid + 1
    
bad = 4
print(firstBadVersion(5))

