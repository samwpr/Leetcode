var isHappy = function(n){
    var seen = {};
    while (n !== 1 && !seen[n]){
        seen[n] = true;
        n = sumOfSqaures(n);
    }
    return n === 1 ? true : false;
};

function sumOfSqaures(numString) {
    return numString.toString().split('').reduce(function(sum, num){
        return sum + Math.pow(num, 2);
    }, 0);
}