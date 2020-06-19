"""
Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.
"""


def make_squares(arr):
    squares = []
    i, j = 0, len(arr) - 1
    while j >= i:
        if abs(arr[i]) > abs(arr[j]):
            squares[:0] = [arr[i] * arr[i]]
            i += 1
        else:
            squares[:0] = [arr[j] * arr[j]]
            j -= 1
    return squares


def main():
    print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
    print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()
