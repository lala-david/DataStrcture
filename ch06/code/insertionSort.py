# InsertionSort
def insertion_Sort(array):
    # index 1 부터 시작하고 전채 배열을 순회 
    for index in range(1, len(array)):
        # index를 position에 할당
        # index에 있는 값을 temp_value에 저장 
        position = index
        temp_value = array[index]
        # postion이 index 0보다 (index 0번쨰)랑 왼쪽 값이 temp에 넣은 변수보다 클 경우 
        while position > 0 and array[position - 1] > temp_value:
            # postion에 왼쪽 값을 저장 
            array[position] = array[position - 1]
            # postion은 -1로 index 낮추기 
            position = position - 1
        # index 0 나오면 while 탈출로 시프트 연산 끝 
        # temp 값 postion에 저장 
        array[position] = temp_value

arr = [4, 2, 7, 1, 3]
insertion_Sort(arr)
print(arr)