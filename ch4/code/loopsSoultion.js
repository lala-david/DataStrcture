// Duplicate in loof soultion 
function hasDuplicateValue(array){
    var existingNumbers = [];
    var cnt = 0; 
    for(var i = 0; i<array.length; i++){
        cnt++; 
        if(existingNumbers[array[i]] === undefined){
            existingNumbers[array[i]] = 1; 
        }
        else{
            return true;
        }
    }
    console.log(cnt)
    return false; 
}

hasDuplicateValue([1,2,3])