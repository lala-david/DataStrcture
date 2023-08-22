def linear_Search (array, value):
    sortArray= sorted(array)
    cnt = 0
    
    for i in sortArray:
        cnt += 1
        if i == value:
            return (value, cnt)
        elif i > value:
            return (None, cnt)

array = [3,75,17,202,80]
value = 202

result, cnt = linear_Search(array, value)

if result is None:
    print("검색 결과: 검색한 값이 없습니다.")
    print("횟수:", cnt)
else:
    print("검색 결과:", result)
    print("횟수:", cnt)
