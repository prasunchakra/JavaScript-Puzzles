"""
Given an array of positive numbers and a positive number ‘k’,
find the maximum sum of any contiguous subarray of size ‘k’.
"""
def max_sub_array_of_size_k(k, arr):
    max_sum, cur_sum, beg, end = 0, 0, 0, 0
    for i in range(len(arr) - 1):
        cur_sum += arr[i]
        end += 1
        if i >= k - 1:
            max_sum = cur_sum if cur_sum > max_sum else max_sum
            cur_sum -= arr[beg]
            beg += 1
    return max_sum


def main():
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))


main()
