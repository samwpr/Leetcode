let isPalindrome = function(x){
    if(x < 0){return false};

    var temp = x;
    var reversed = 0; 

    while(x > 0){
        reversed = (reversed * 10) + (x % 10);
        x = parseInt(x/10); //Why is there a need to parseInt here? 
    }
    return reversed == temp
};

console.log(isPalindrome(123))
