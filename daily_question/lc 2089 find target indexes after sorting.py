"""
2089. Find Target Indices After Sorting Array
Solved
Easy
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed integer array nums and a target element target.

A target index is an index i such that nums[i] == target.

Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

 

Example 1:

Input: nums = [1,2,5,2,3], target = 2
Output: [1,2]
Explanation: After sorting, nums is [1,2,2,3,5].
The indices where nums[i] == 2 are 1 and 2.
Example 2:

Input: nums = [1,2,5,2,3], target = 3
Output: [3]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 3 is 3.
Example 3:

Input: nums = [1,2,5,2,3], target = 5
Output: [4]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 5 is 4.
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i], target <= 100
"""

# Method 1

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        result=[]
        for i in range(len(nums)):
            if nums[i]==target:
                result.append(i)
        return result

# Time Complexity O(nlogn)+O(n)

# MEthod 2

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        count_smaller=0
        count_target=0
        for i in nums:
            if i<target:
                count_smaller+=1
            elif i==target:
                count_target+=1
        return list(range(count_smaller,count_smaller+count_target))
       

# Time Complexity: O(n) - optimal approach

