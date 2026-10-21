import heapq
"""
Given an integer array arr[] and an integer k, find and return the kth smallest element in the given array.

Examples :

Input: arr[] = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10], k = 4
Output: 5
Explanation: 4th smallest element in the given array is 5.
Input: arr[] = [7, 10, 4, 3, 20, 15], k = 3
Output: 7
Explanation: 3rd smallest element in the given array is 7.
Constraints:

1 ≤ arr.size(), arr[i] ≤ 105
1 ≤ k ≤ arr.size()
"""
class Solution:
    def kthSmallest(self, arr, k):
        # Code here
        # heap=[]
        # for i in arr:
        #     heapq.heappush(heap,i)
        # for i in range(1,k+1):
        #     if i==k:
        #         return heapq.heappop(heap)
        #     heapq.heappop(heap)
        heapq.heapify(arr)

        for _ in range(k - 1):
            heapq.heappop(arr)

        return heapq.heappop(arr)
        
"""
Note: heapiy inserts in O(n) whole array if i use heappush it does in O(nlogn)
"""