"""
You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.

Return the index of the peak element.

Your task is to solve it in O(log(n)) time complexity.

 

Example 1:

Input: arr = [0,1,0]

Output: 1

Example 2:

Input: arr = [0,2,1,0]

Output: 1

Example 3:

Input: arr = [0,10,5,2]

Output: 1

 

Constraints:

3 <= arr.length <= 105
0 <= arr[i] <= 106
arr is guaranteed to be a mountain array.
"""

## clean code
def peakIndexInMountainArray(arr: list[int]) -> int:
    low = 0
    high = len(arr) - 1

    while low < high:
        guess = (low + high) // 2

        if arr[guess] > arr[guess + 1]:
            high = guess
        else:
            low = guess + 1

    return low 

## my fist pass code, not so clean, extra conditions but still logn

def peakIndexInMountainArray(arr: list[int]) -> int:
    low=0
    high=len(arr)-1
    while low<=high:
        guess=(low+high)//2
        if guess<low:
            low=guess+1
        elif guess>high:
            high=guess-1
        else:
            if arr[guess-1]<arr[guess] and arr[guess+1]<arr[guess]:
                return guess
            elif arr[guess-1]>arr[guess]:
                high=guess
            else:
                low=guess+1