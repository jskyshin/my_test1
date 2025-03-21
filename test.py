# this script is used for practice of coding for interview


#### 1. Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
# Follow-up: Can you do this in O(N) time and constant space?

def largest_sum(lst):

    if len(lst) == 0:
        return 0
    elif len(lst) == 1:
        return lst[0]
    elif len(lst) == 2:
        return max(lst)

    max_sum = 0
    for i in range(len(lst)):
        sum = lst[i]
        for j in range(i+2, len(lst)):
            sum += lst[j]
            if sum > max_sum:
                max_sum = sum
    print(max_sum)


#### 2. Given a list of elements, find the majority element, which appears more than half the time (> floor(len(lst) / 2.0)).
# You can assume that such element exists.
# For example, given [1, 2, 1, 1, 3, 4, 0], return 1.

from math import floor

def find_majority(lts):
    stored_num  = dict()
    half = floor(len(lts) / 2.0)
    for i in lts:
        if i in stored_num:
            if stored_num[i] + 1 >= half:
                print(i)
                return
            stored_num[i] += 1
        else:
            stored_num[i] = 1


if __name__ == '__main__':


    # March 16, 2025
    lts = [1, 2, 1, 1, 3, 4, 0]
    find_majority(lts)

    # March 16, 2025: test for the first question
    lst = [2, 4, 6, 2, 5]
    largest_sum(lst)
    lst = [5, 1, 1, 5]
    largest_sum(lst)
    lst = [1, 2, 3, 4, 5, 6]
    largest_sum(lst)
    lst = [1, 2, 3, 4, 5, 6, 7]
    largest_sum(lst)


