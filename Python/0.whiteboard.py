def makeGood(s: str) -> str:
    stack = []
    for i in s:
        stack.append(i)

    for j in range(len(stack) - 1):
        if stack[j].upper() == stack[j + 1]:
            stack.pop(j)
            stack.pop(j + 1)

    print(stack)
        
makeGood("leEeetcode")