'''
Link: https://leetcode.com/problems/largest-perimeter-triangle/
Companies: Tesla
Level: Easy 
'''


class Solution:
    def largestPerimeter(self, nums) -> int:
        x = sorted(nums, reverse=True)
        print(x)
        for i in range(3, len(x)+1):
            print("i = ", i)
            print("x[i - 3]", x[i - 3])
            print("x[i - 2]", x[i - 2])
            print("x[i - 1]", x[i - 1])
            print("")
            if (x[i - 3] < x[i - 2] + x[i - 1]):
                return sum(x[i-3:i])
        return 0





        

obj = Solution()
nums1 = [2,1,2] #5
nums2 = [1,2,1] #0
nums3 = [3,2,3,4] #10
nums4 = [3,6,2,3] #8
print(obj.largestPerimeter(nums1))
print(obj.largestPerimeter(nums2))
print(obj.largestPerimeter(nums3))
print(obj.largestPerimeter(nums4))

