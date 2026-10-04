"""
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "(*)"
Output: true
Example 3:

Input: s = "(*))"
Output: true
Example 4:

Input: s = "("
Output: false
 

Constraints:

1 <= s.length <= 100
s[i] is '(', ')' or '*'.
"""
def checkValidString(s: str) -> bool:
        open_st = []
        star_st = []

        for i, ch in enumerate(s):
             if ch == '(':
                 open_st.append(i)

             elif ch == '*':
                 star_st.append(i)

             else:  # ')'
                if open_st:
                    open_st.pop()
                elif star_st:
                    star_st.pop()
                else:
                    return False

    # Match remaining '(' with '*' that occur after them
        while open_st and star_st:
            if open_st[-1] < star_st[-1]:
                open_st.pop()
                star_st.pop()
            else:
                return False

        return len(open_st) == 0