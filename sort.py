def merge(list_x, list_y, start, mid, end):
    list_x_left = []
    list_x_right = []
    list_y_left = []
    list_y_right = []

    list_x_left.extend(list_x[start:mid+1])
    list_x_right.extend(list_x[mid+1:end+1])
    list_y_left.extend(list_y[start:mid+1])
    list_y_right.extend(list_y[mid+1:end+1])
    
    i = 0
    j = 0
    k = start

    while(i < len(list_x_left) and j < len(list_x_right)):
        if(list_x_left[i] < list_x_right[j]):
            list_x[k] = list_x_left[i]
            list_y[k] = list_y_left[i]
            i += 1
        else:
            list_x[k] = list_x_right[j]
            list_y[k] = list_y_right[j]
            j += 1
        k += 1

    while(i < len(list_x_left)):
        list_x[k] = list_x_left[i]
        list_y[k] = list_y_left[i]
        i += 1
        k += 1

    while(j < len(list_x_right)):
        list_x[k] = list_x_right[j]
        list_y[k] = list_y_right[j]
        j += 1
        k += 1     
    return 

def merge_sort(list_x, list_y, start, end):
    if(start < end):
        mid = int(start + ((end - start) / 2.0))
        merge_sort(list_x, list_y, start, mid)
        merge_sort(list_x, list_y, mid+1, end)
        merge(list_x, list_y, start, mid, end)
    return
