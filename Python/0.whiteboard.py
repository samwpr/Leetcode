def isPalindrome(x: int) -> bool:
    if x < 0:
        return False 
    
    reverse = 0
    temp = x
    while temp != 0:
        x = temp % 10 
        reverse = reverse * 10 + x
        temp = temp // 10 
    
    print(reverse)
    
    if reverse == x:
        return True 
    else:
        return False 

print(isPalindrome(121))