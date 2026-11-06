"""
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

 

Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
"""

class Solution:
    def reorganizeString(self, s: str) -> str:
        # import heapq

        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        heap = []

        for ch, cnt in freq.items():
            heapq.heappush(heap, (-cnt, ch))

        res = []
        prev_ch = ""

        while heap:
            cnt, ch = heapq.heappop(heap)

            # Can place the most frequent character
            if not res or ch != prev_ch:
                res.append(ch)
                cnt += 1

                if cnt < 0:
                    heapq.heappush(heap, (cnt, ch))

                prev_ch = ch

            else:
                # Need another character
                if not heap:
                    return ""

                cnt2, ch2 = heapq.heappop(heap)

                res.append(ch2)
                cnt2 += 1

                if cnt2 < 0:
                    heapq.heappush(heap, (cnt2, ch2))

                # Put skipped character back
                heapq.heappush(heap, (cnt, ch))

                prev_ch = ch2

        return "".join(res)

  """
  time:O(nlogk)
  space: O(n)
  """
