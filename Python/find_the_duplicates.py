# M ≈ N - the array lengths are approximately the same
def find_duplicates(arr1, arr2):
  dup = [] 
  p1 = 0
  p2 = 0
  
  while p1 < len(arr1) and p2 < len(arr2):
    if arr1[p1] == arr2[p2]:
      dup.append(arr1[p1])
      p1 += 1
      p2 += 1
    elif arr1[p1] != arr2[p2]:
      p1 += 1
    else:
      p2 += 1
  return dup

'''
Approach: 
Use pointers as they are commonly used for traversing and comparing elements in two sorted arrays. Doing so we do not need to store additional data or perform additional operations. 

For example if we were to brute force and compare every element of the two array for duplicates this would result in a time complexity of O(N^2) however the space complexity would still be O(1) 

Another inefficient way is to use a merge sort approach to find the duplicate which will give us a time complexity of O(N * log N) due to sorting and additional O(N) time complexity to compare the elements and find the duplicates. This will give us a space complexity of O(N) as additional space is required to store the merged arrays. 

Space complexity is O(N) in the worst case it will be as big as the smaller input array.

Time complexity is O(N + M) because both arrays are iterated through once, the time taken to increment the pointers and check that the conditions is constant. As such the time complexity is linear in the size of the input arrays. 

Also each iteration of the while loop increments either p1 or p2, meaning to say the loop will run at most N times which will be the length of the shorter array seeing that the arrays are sorted. 
'''


# M ≫ N - arr2 is much bigger than arr1.
def find_duplicates_2(arr1, arr2):
    dup = []
    for i in range(len(arr1)):
        if binarySearch(arr2, arr1[i]) != -1:
            dup.append(arr1[i])
    return dup
    

def binarySearch(arr, target):
    left = 0
    right = len(arr) -1
    while left <= right:
        mid = (left + right) //2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1 

'''
The time complexity is O(N Log M) 

The time complexity for binary search is O(Log M) because we perform binary search for each N element in the smaller array the total time complexity is O(N Log M)

The space complexity remains the same as case 1 at O(N) where at worst it will be as big as the smaller input array.
'''


'''
Comparing the two approaches. 

While binay search can be used for the first case we do not do so as it has a worst time complexity. 

Where one array is signficantly large than the other the time complexity will be dominated by the larger array as such we will not use pointers as doing so will give us a time complexity of O(N * M) as we need to iterate through both arrays and comapre the elemets at each position. which is worst than O(N log M)
'''