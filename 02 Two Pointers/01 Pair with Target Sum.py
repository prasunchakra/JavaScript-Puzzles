"""
Given an array of sorted numbers and a target sum,
find a pair in the array whose sum is equal to the given target.
Write a function to return the indices of the two numbers
(i.e. the pair) such that they add up to the given target.
"""


def pair_with_targetsum(arr, target_sum):
    i, j = 0, len(arr) - 1
    while j > i:
        sum = arr[i] + arr[j]
        if sum == target_sum:
            return [i, j]
        elif sum > target_sum:
            j -= 1
        else:
            i += 1
    return [-1, -1]


def main():
    print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum([2, 5, 9, 11], 11))


main()
