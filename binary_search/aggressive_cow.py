"""
Given an integer array arr[], which denotes the positions of stalls. All the positions are distinct. There are k aggressive cows.

Assign the cows to the stalls such that the minimum distance between any two cows is maximized.

Examples:

Input: arr[] = [1, 2, 4, 8, 9], k = 3
Output: 3
Explanation: The first cow can be placed at arr[0], the second at arr[2], and the third at arr[3]. The minimum distance between any two cows is 3 (between arr[0] and arr[2]), which is the maximum possible among all valid arrangements.
Input: arr[] = [10, 1, 2, 7, 5], k = 3
Output: 4
Explanation: The first cow can be placed at arr[0], the second at arr[1], and the third at arr[4]. In this arrangement, the minimum distance between any two cows is 4 (between arr[1] and arr[4]), which is the maximum possible among all valid arrangements.
Constraints:

arr.size() ≤ 106
0 ≤ arr[i] ≤ 108
2 ≤ k ≤ arr.size()
"""

class Solution:
    def aggressiveCows(self, arr, k):
        # code here
        arr.sort()

        low = 1
        high = arr[-1] - arr[0]
        result = 0

        while low <= high:
            guess = (low + high) // 2

            count = 1
            last_position = arr[0]

            for i in range(1, len(arr)):
                if arr[i] - last_position >= guess:
                    count += 1
                    last_position = arr[i]

            if count >= k:
                result = guess
                low = guess + 1
            else:
                high = guess - 1

        return result