const twoSum = (array, goal) => {
    let indexes = [];

    for(let i = 0; i < array.length; i++){

       for(let j = i + 1; j < array.length; j++){

          if (array[i] + array[j] === goal) {
            indexes.push(i);
            indexes.push(j);
          }
       }
    }
    return indexes;
}

var array = [1, 3, 10, 11, 14];
var goal = 13

console.log(twoSum(array, goal));

