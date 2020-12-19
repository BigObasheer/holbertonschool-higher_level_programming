#!/usr/bin/python3
""" finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ find peak  """
    nums = list_of_integers
    length = len(nums)

    if nums == []:
        return None
    if nums == 1:
        return (lis[0])

    for i in range(0, length - 1):
        if nums[i] > nums[i + 1]:
            return (nums[i])
    return (nums[i + 1])
