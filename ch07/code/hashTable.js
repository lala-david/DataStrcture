// O(N)
function hasDuplicateValue(array) {
    var cnt = 0;
    var existingValues = {};
    for(var i = 0; i < array.length; i++){
        if(existingValues[array[i]] === undefined){
            existingValues[array[i]] = 1;
        }
        else{
            return true;
        }
    }
    console.log(existingValues)
    return false;
}

hasDuplicateValue([1,2,3])