def binary_search(array, value, start, end):
    sortArray = sorted(array)
    cnt = 0 

    while start<=end:
        midPoint = (start+end) // 2

        cnt+=1 

        if sortArray[midPoint] == value:
            return (midPoint, cnt) 
        
        elif sortArray[midPoint] > value:
            end = midPoint-1
        
        elif sortArray[midPoint] < value:
            start = midPoint+1 

    return None
    
arr = [16, 2, 6, 4, 9, 7, 10, 14, 13]
val = 7 
sta = 0 
ed = len(arr)-1 

power = binary_search(arr, val, sta, ed)

if power is None:
    print("검색 결과: 검색한 값이 없습니다")
else: 
    print("{}번쨰 인덱스에 있습니다.".format(power[0]))
    print("검색 횟수:", power[1])
