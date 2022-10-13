def testFunc1():
    res = 0
    def testFunc2():
        nonlocal res 
        res = 1

    testFunc2()
    return res 

print(testFunc1())