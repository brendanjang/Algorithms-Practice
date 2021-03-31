# binary search algorithm
# params: list and item to search for
def binary_search(list, item):
    # low and high values to keep track of which part of list to search
    low = 0
    high = len(list) - 1

    # while not narrowed down to 1 element
    while low <= high:
        # start with checking middle (index) element
        mid = (low + high) // 2
        guess = list[mid]

        # if middle element is correct element, return element
        if guess == item:
            # return index of item
            return mid
        # if guess is too high, new high value is 1 less than mid val
        if guess > item:
            high = mid - 1
        # if guess is too low, new low value is 1 more than mid val
        else:
            low = mid + 1
    # if item not in list, return null
    return None


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 9))
print(binary_search(my_list, -1))
