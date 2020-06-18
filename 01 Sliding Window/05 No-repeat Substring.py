def non_repeat_substring(str):
    beg, max_sub_len = 0, 0
    location = {}
    for i, val in enumerate(str):
        if val in location:
            beg = max(beg, location[val] + 1)
        location[val] = i
        max_sub_len = max(max_sub_len, i - beg + 1)
    return max_sub_len


def main():
    """
    Given a string, find the length of the longest substring which has no repeating characters.
    """
    print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abccde")))


main()
