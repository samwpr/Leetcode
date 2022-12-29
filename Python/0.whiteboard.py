def find_duplicates(arr1, arr2):
    dup = []
    p1 = 0
    p2 = 0
    while p1 < len(arr1) and p2 < len(arr2):
        #0 < 6 and 0 < 5
        #1 < 6 and 0 < 5
        #2 < 6 and 0 < 5 
        #3 < 6 and 1 < 5 
        #4 < 6 and 1 < 5
        #5 < 6 and 2 < 5
        #6 < 6 # False -> return dup 
        if arr1[p1] == arr2[p2]:
            #1 == 3 False
            #2 == 3 False  
            #3 == 3 True 
            #5 == 6 False
            #6 == 6 True
            #7 == 7 True   
            dup.append(arr1[p1])
            p1 += 1
            #p1 = 3 
            #p1 = 5
            #p1 = 6
            p2 += 1
            #p2 = 1
            #p2 = 2
            #p2 = 3  
        elif arr1[p1] < arr2[p2]:
            #1 < 3
            #2 < 3 
            #5 < 6 
            p1 += 1
            #p1 = 1
            #p1 = 2
            #p1 = 4   
        else:
            p2 += 1
    return dup

arr1 = [1, 2, 3, 5, 6, 7]
arr2 = [3, 6, 7, 8, 20]

print(find_duplicates(arr1, arr2))

#print(len(arr1)) #6
#print(len(arr2)) #5
