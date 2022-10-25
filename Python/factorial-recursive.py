from tkinter import N


def factorial(n):
    if n < 0: return -1 

    if n < 2: return 1

    n = n*factorial(n - 1)
    return n

print(factorial(5))