#https://www.pythonpool.com/python-for-loop-decrement/
#https://www.youtube.com/watch?v=9TlHvipP5yA&ab_channel=AbdulBari 
#5:50 

#Say n is 10 the loop will increase from 1 to 10. Hence time complexity is O(n)
def o_n_1(n): 
    for i in range(0, n, 1):
        print(i) #This statment will execute n times 


#Say n is 10 the loop will decrease from 10 to 1. Hence time complexity is O(n)
def o_n_2(n): #O(n)
    for i in range(n, 0, -1):
        print(i) #This statment will execute n times 


#Say n is 10 the loop will increase from 1 to 10 but in steps of two. f(n) = n/2, the degree of polynomial (largest exponent) is n hence is O(n)
def o_n_3(n):
    for i in range(0, n, 2):
        print(i)


#Say n is 10 the first loop will increase by 1, then the second loop will increase from 1 to 10. Once the second loop has reached 10, it will exit and go back to the first loop where and the process will continue till the first loop reaches 10. Hence it is O(n^2)
def o_n_square_1(n):
    for i in range(0, n, 1): #n + 1
        for j in range(0, n, 1): #n x n+1
            print(j) #n x n


