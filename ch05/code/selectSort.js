// selection Sort 
function selectionSort(array) {
    // 외부 for 문 
    for(var i = 0; i < array.length; i++){
        // 첫 번째 인덱스 
        var lowestNumberIndex = i;
        // 내부 for 문 
        // 두 번째 index를 첫 번째 index 비교 
        // 첫 번째 index가 두 번째 index보다 크면 lowestNumberIndex에 두 번째 인덱스 저장  
        for(var j = i+1; j < array.length; j++){
            if(array[j] < array[lowestNumberIndex]){
                lowestNumberIndex = j;
            }
        }
        // 첫 번째 인덱스랑 low 변수가 다르면 교환 
        // 첫 번째 인덱스에 temp 변수에 저장 
        // low 변수를 첫 번째 인덱스에 저장 
        // temp에 저장된 변수를 low에 저장  
        if(lowestNumberIndex !=i){
            var temp = array[i];
            array[i] = array[lowestNumberIndex];
            array[lowestNumberIndex] = temp;
        }
    }
    // 반환 
    return array; 
}

var arr = [4,5,3,1,2]
selectionSort(arr)
console.log(arr)