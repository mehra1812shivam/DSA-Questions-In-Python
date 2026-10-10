"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        row=-1
        low=0
        high=n-1
        while low<=high:
            guess=(low+high)//2
            if matrix[guess][0]<=target:
                row=guess
                low=guess+1
            else:
                high=guess-1
        if row==-1:
            return False
        low=0
        high=m-1
        while low<=high:
            guess=(low+high)//2
            if matrix[row][guess]==target:
                return True
            elif matrix[row][guess]<target:
                low=guess+1
            else:
                high=guess-1
        return False

"""

Approach
Current:
Binary Search
/
Array
Suggested:
Binary Search
/
Array
Key Idea:
Use binary search to find the target row, then search within that row.
"""        

# In Single binary search

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        low=0
        high=(n*m)-1
        while low<=high:
            guess=(low+high)//2
            row=guess//m
            col=guess%m
            
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                low=guess+1
            else:
                high=guess-1
        return False
        