#https://www.pythonpool.com/python-for-loop-decrement/
#https://www.youtube.com/watch?v=9TlHvipP5yA&ab_channel=AbdulBari 
#2:45

#Say n is 10 the loop will increase from 1 to 10. Hence time complexity is O(n)
def O_n_1(n): 
    for i in range(0, n):
        print(i) #This statment will execute n times 


#Say n is 10 the loop will decrease from 10 to 1. Hence time complexity is O(n)
def O_n_2(n): #O(n)
    for i in range(n, 0, -1):
        print(i) #This statment will execute n times 


#Say n is 10 the loop will increase from 1 to 10 but in steps of two. f(n) = n/2, the degree of polynomial (largest exponent) is n hence is O(n)
def O_n_3(n):
    for i in range(0, n, 2):
        print(i)


