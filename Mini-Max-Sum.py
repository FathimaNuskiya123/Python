# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.
#
# Input Format
#
# A single line of five space-separated integers.
#
# Constraints
#
# Each integer is in the inclusive range .
# Output Format
#
# Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)
#
# Sample Input
#
# 1 2 3 4 5
# Sample Output
#
# 10 14
# Explanation
#
# Our initial numbers are , , , , and . We can calculate the following sums using four of the five integers:
#
# If we sum everything except , our sum is .
# If we sum everything except , our sum is .
# If we sum everything except , our sum is .
# If we sum everything except , our sum is .
# If we sum everything except , our sum is .
# Hints: Beware of integer overflow! Use 64-bit Integer.


def minimaxsum(arr):
    # print(arr)
    length = len(arr)
    final_list = []
    for i in range(0,length):
        new_arr = arr[0:length]
        new_arr[i]=0
        append_sum = sum(new_arr)
        final_list.append(append_sum)
    print(min(final_list),max(final_list))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    minimaxsum(arr)