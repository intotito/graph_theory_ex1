import math
def quickSort(list: list, start: int, stop: int) -> list:
    i_pivot = stop
    pivot = list[i_pivot]
    i = start
    count = 0
    while(i < i_pivot):
        count += 1
        temp = list[i]
    #    print('XXXXXX', 'i=', i, 'list[i]=', list[i])
        if(list[i] > pivot):
            print('i=', i, 'i_pivot=', i_pivot, 'pivot=', pivot, 'list[i]=', list[i])
            list[i] = list[i_pivot - 1]
            list[i_pivot] = temp
            i_pivot -= 1
            list[i_pivot] = pivot
        else:
            i += 1
            print('increment at', i)
    if((i_pivot - 1) - start > 0):
        quickSort(list, start, i_pivot - 1)
    if(stop - (i_pivot + 1) > 0):
        quickSort(list, i_pivot + 1, stop)
    print('Count =', count, 'i_pivot=', i_pivot, 'i=', i)
    return list

list =[2, 43, 52, -4, -5, 34, 8, 23, 14, 16, 4, 3, 1, -5, 0, -88]

print(quickSort(list, 0, len(list) - 1))