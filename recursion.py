# using recursion for sum
def sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sum(arr[1:])


print(sum([1, 3, 5, 7, 9]))


# count numbers of items in a list using recursion
def count(arr):
    if len(arr) == 0:
        return 0
    else:
        return 1 + count(arr[1:])


print(count([1, 3, 5, 7, 9, 10]))

