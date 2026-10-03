"""
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

 

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.
"""
"Approach taken:"
"we will store index in stack as soon as invalid parenthesis string happnes we put new index as median"
""

def longestValidParentheses( s):
    st = [-1]
    max_length = 0

    for i in range(len(s)):
        if s[i] == '(':
            st.append(i)
        else:
            st.pop()

            if not st:
                st.append(i)
            else:
                max_length = max(max_length, i - st[-1])

    return max_length