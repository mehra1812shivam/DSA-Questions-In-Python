""""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
 

Constraints:

1 <= text.length <= 104
text consists of lower case English letters only.
"""


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        h_map = {}
        s_map = {}

        for ch in "balloon":
            s_map[ch] = s_map.get(ch, 0) + 1

        for ch in text:
            h_map[ch] = h_map.get(ch, 0) + 1

        min_value = float('inf')

        for ch in s_map:
            if ch not in h_map:
                return 0

            min_value = min(min_value, h_map[ch] // s_map[ch])

        return min_value

        