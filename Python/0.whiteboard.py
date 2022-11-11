def climbstair(n):
    one, two = 1, 1

    for i in range(n - 1):
        temp = one
        one = one + two
        two = temp
        print("temp", temp)
        print("one", one)
        print("two", two)
        print("-----")
    return one

climbstair(5)