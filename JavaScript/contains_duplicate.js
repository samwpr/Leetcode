var containsDuplicate = function (nums){
    const hashTable = new Map();

    for (let i = 0; i < nums.length; i++){
        if (hashTable.has(nums[i])) return true;
        else hashTable.set(nums[i], true);
    }
    return false;
}

nums = [1, 2, 3]
x = containsDuplicate(nums);
console.log(x);

