"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
Example 1:
Input: "()"
Output: True
Example 2:
Input: "()[]{}"
Output: True
Example 3:
Input: "(]"
Output: False
Example 4:
Input: "([)]"
Output: False
Example 5:
Input: "{[]}"
Output: True
"""
word = "{[]}"

while True :
    if "()" in word or "[]" in word or "{}" in word :
        
        word = "".join(word.split("()"))
        word = "".join(word.split("[]"))
        word = "".join(word.split("{}"))
    else :
        break
print(not word)

    
    




