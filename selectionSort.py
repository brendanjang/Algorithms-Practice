# sort an array from smallest to largest
def find_smallest(arr):
    # stores the smallest value
    smallest = arr[0]
    # stores the index of the smallest value
    smallest_index = 0
    for i in range(1, len(arr)):
        # if value at index arr[i] is less than smallest value then
        # new smallest = arr[i] and new index = i
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


# function for selection sort
def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        # find smallest element in array
        smallest = find_smallest(arr)
        # append smallest element to end of new array
        new_arr.append(arr.pop(smallest))
    return new_arr


print(selection_sort([5, 3, 6, 2, 10]))
