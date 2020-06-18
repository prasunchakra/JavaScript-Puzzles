"""
Given a string, find the length of the longest substring in it with no more than K distinct characters.
"""


def longest_substring_with_k_distinct(str1, k):
    char_freq = {}
    beg, long_len, cur_len = 0, 0, 0
    for i, char in enumerate(str1):
        if char not in char_freq:
            char_freq[char] = 0
        char_freq[char] += 1
        cur_len += 1
        while len(char_freq) > k:
            cur_len -= 1
            beg_char = str1[beg]
            char_freq[beg_char] -= 1
            if char_freq[beg_char] == 0:
                del char_freq[beg_char]
            beg += 1
        long_len = max(long_len, cur_len)
    return long_len


def main():
    print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()
