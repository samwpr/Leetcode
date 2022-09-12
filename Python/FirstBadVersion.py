# https://leetcode.com/problems/first-bad-version/

bad = 0
def isBadVersion(version):
    if version >= bad:
        return True
    return False

def firstBadVersion(n):
    if n < 2:
        return n
    start = 1
    end = n
    while (start <= end):
        mid = (start + end)//2
        if isBadVersion(mid) == True and isBadVersion(mid-1) == False:
            return mid
        elif isBadVersion(mid-1) == True:
            end = mid -1
        else:
            start = mid+1

bad = 4
print(firstBadVersion(5))

