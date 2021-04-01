def quicksort(array):
    # base cases when arrays have 0 or 1 element don't need sorting
    if len(array) < 2:
        return array
    else:
        # recursive case
        pivot = array[0]
        # sub-array of all elements less than the pivot
        less = [i for i in array[1:] if i <= pivot]

        # sub-array of all elements greater than the pivot
        greater = [i for i in array[1:] if i > pivot]

        # recursive call + combine
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([10, 5, 2, 3]))