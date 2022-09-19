'''
https://leetcode.com/problems/snapshot-array/
Level: Medium 
Companies: Google, Rubrik

Input: ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
Output: [null,null,0,null,5]
Explanation: 
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
'''

from collections import defaultdict
class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.history = defaultdict(dict)

    def set(self, index: int, value: int):
        self.history[self.snap_id][index] = value
    
    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int: 
        for i in range(snap_id, -1, -1):
            if index in self.history[i]: 
                return self.history[i][index]
        return 0


ob = SnapshotArray(3) 
ob.set(0, 5)
print(ob.snap()) #Print 0
ob.set(0,6)
print(ob.get(0,0)) #Print 5 
    


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)


