// intersection
function intersection(first_array, second_array){
    var result = [];

    for (var i = 0; i<first_array.length; i++){
        for (var j = 0; j<second_array.length; j++){
            if(first_array[i]==second_array[j]){
                result.push(first_array[i]);
                break;
            }
        }
    }
    console.log(result)
    return result;
}
var a = [3, 1, 4, 2]
var b = [4, 5, 3, 6]
intersection(a, b)
