# selection Sort 
def selection_Sort(array): 
    for i in range(len(array)):
        minn = i
        for j in range(i+1, len(array)):
            if array[j] < array[minn]:
                minn = j
        array[i], array[minn] = array[minn], array[i]


array = [3,2,1]
selection_Sort(array)
print(array)
