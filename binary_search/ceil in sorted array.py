"""
Given a sorted array arr[] and an integer x, find the index (0-based) of the smallest element in arr[] that is greater than or equal to x. This element is called the ceil of x. If such an element does not exist, return -1.

Note: In case of multiple occurrences of ceil of x, return the index of the first occurrence.

Examples

Input: arr[] = [1, 2, 8, 10, 11, 12, 19], x = 5
Output: 2
Explanation: Smallest number greater than 5 is 8, whose index is 2.
Input: arr[] = [1, 2, 8, 10, 11, 12, 19], x = 20
Output: -1
Explanation: No element greater than 20 is found. So output is -1.
Input: arr[] = [1, 1, 2, 8, 10, 11, 12, 19], x = 0
Output: 0
Explanation: Smallest number greater than 0 is 1, whose indices are 0 and 1. The index of the first occurrence is 0.
Constraints:

1 ≤ arr.size(), arr[i] ≤ 106
0 ≤ x ≤ 106
"""

def findceil(nums,x):
    low=0
    high=len(nums)-1
    lowest_index=float('inf')
    while low<=high:
        guess=(low+high)//2
        if nums[guess]<x:
            low=guess+1
        else:
            high=guess-1
            lowest_index=min(lowest_index,guess)
    if lowest_index==float('inf'):
        return -1
    else:
        return lowest_index


