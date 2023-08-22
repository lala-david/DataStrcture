// Duplicate in array 
function hasDuplicateValue(array) {
    var cnt = 0;
    for(var i = 0; i < array.length; i++){
        for(var j = 0; j< array.length; j++) {
            cnt++; 
            if (i !== j && array[i] == array[j])
            return true;
        }
    }
    console.log(cnt)
    return false;
}

hasDuplicateValue([1,2,3])