"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""

def searchRange(nums,target):
    low=0
    high=len(nums)-1
    result=[]
    while low<=high:
        guess=(low+high)//2
        if nums[guess]<target:
            low=guess+1
        elif nums[guess]>target:
            high=guess-1
        else:
            high=guess-1
    if low==len(nums)or nums[low] != target:
        result.append(-1)
    else:
        result.append(low)
    low=0
    high=len(nums)-1
    while low<=high:
        guess=(low+high)//2
        if nums[guess]<=target:
            low=guess+1
        else:
            high=guess-1
        
    if high<0 or nums[high] != target:
        result.append(-1)
    else:
        result.append(high)
    return result
