"""
Given an array of sorted numbers, remove all duplicates from it.
 You should not use any extra space; after removing the
 duplicates in-place return the new length of the array.
"""


def remove_duplicates(arr):
    end, i = 0, 1
    while i < len(arr):
        if arr[end] != arr[i]:
            end += 1
            arr[end] = arr[i]
        i += 1
    return end + 1


def main():
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))


main()
