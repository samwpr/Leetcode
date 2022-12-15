def climbStair(n):
    one = 1
    two = 1

    for i in range(n - 1):
        temp = one 
        one = one + two
        two = temp

    return one

print(climbStair(4))


for i in range(3 - 1):
    print("lol")