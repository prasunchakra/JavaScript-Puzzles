"""
Given an array of positive numbers and a positive number ‘S’,
find the length of the smallest contiguous subarray whose
sum is greater than or equal to ‘S’. Return 0,
if no such subarray exists.
"""
def smallest_subarray_with_given_sum(s, arr):
    min_len, cur_sum, beg, end = len(arr), 0, 0, 0
    for i in range(len(arr)):
        cur_sum += arr[i]
        end += 1
        while cur_sum >= s:
            min_len = min_len if min_len < (end - beg) else (end - beg)
            cur_sum -= arr[beg]
            beg += 1
    return min_len


def main():
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))


main()

