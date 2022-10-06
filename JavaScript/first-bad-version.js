var bad = 0

function isBadVersion(version){
    if(version >= bad){
        return true;
    } else {
        return false;
    }
}

function firstBadVersion(isBadVersion){
    return function(n){
        var start = 1;
        var end = n;
        var mid = parseInt(n/2);

        while(start<end){
            if(!isBadVersion(mid)){
                start = mid + 1;
            } else {
                end = mid
            }
            mid = parseInt((start + end) / 2);
        }
        return start;
    };
};


bad = 4 
console.log(firstBadVersion(5));