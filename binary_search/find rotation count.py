"""
Given an increasing sorted rotated array arr[] of distinct integers. The array is right-rotated k times. Find the value of k.

Examples:

Input: arr[] = [5, 1, 2, 3, 4]
Output: 1
Explanation: The given array is [5, 1, 2, 3, 4]. The original sorted array is [1, 2, 3, 4, 5]. We can see that the array was rotated 1 times to the right.
Input: arr = [1, 2, 3, 4, 5]
Output: 0
Explanation: The given array is not rotated.
Input: arr = [6, 9, 2, 4]
Output: 2
Explanation: The original array is [2, 4, 6, 9] and we get the above array after two rotations.
"""

class Solution:
    def findKRotation(self, arr):
        # code here
        low=0
        high=len(arr)-1

        while low<high:
            guess=(low+high)//2
            if arr[guess] > arr[high]:
                low = guess + 1
            else:
                high = guess

        return low 