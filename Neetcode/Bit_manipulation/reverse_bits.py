class Solution:
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            res = res << 1
            if n % 2 == 1:
                res += 1
            n = n >> 1
        return res 

obj = Solution()
print(obj.reverseBits(11111111111111111111111111111101))

'''
Explanation:
n = 11111111111111111111111111111101

1st Loop:
res = 0
res = res << 1: res = 0, there is no actual bit to shift, the value of res remains 0.
if n%2 == 1: The last bit of n is 1, 1 % 2 == 1, this statement evaluates to true, hence the inner statement will be executed.
res += 1: res = 1
n = n >> 1: The rightmost bit will be dropped and will become: 1111111111111111111111111111110

2nd Loop:
res = 1
res = res << 1: res = 10
if n%2 == 1: The last bit of n is 0, 0 % 2 == 0, this statement evaluates to false, hence the inner statement will not execute.
n = n >> 1: The rightmost bit will be dropped and will become: 111111111111111111111111111111

3rd Loop:
res = 10
res = res << 1: res = 100
if n%2 == 1: The last bit of n is 1, 1 % 2 == 1, this statement evaluates to true, hence the inner statement will be executed.
res += 1: res = 101
n = n >> 1: The rightmost bit will be dropped and will become: 11111111111111111111111111111

4th Loop:
res = 101
res = res << 1: res = 1010
if n%2 == 1: The last bit of n is 1, 1 % 2 == 1, this statement evaluates to true, hence the inner statement will be executed.
res += 1: res = 1011
n = n >> 1: The rightmost bit will be dropped and will become: 1111111111111111111111111111
'''