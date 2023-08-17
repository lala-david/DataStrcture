# BubbleSort 
def bubble_sort(list):
    # final index element value  
    unsorted_until_index = len(list) - 1
    # False [⏩]
    sorted = False

    # Repeat to sorted 
    while not sorted:
        sorted = True
        for i in range(unsorted_until_index):
            # list 0 > list 1 ⏩ exchange list[1] <-> list[0] 
            if list[i] > list[i+1]:
                sorted = False
                list[i], list[i+1] = list[i+1], list[i]
        # max value is sorted ⏩ un - 1 
        unsorted_until_index = unsorted_until_index - 1

list = [65, 55, 45, 35, 25, 15, 10]
bubble_sort(list)
print(list) 
