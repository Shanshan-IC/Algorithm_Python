"""
https://leetcode.com/problems/reverse-words-in-a-string/description/

For example,
Given s = "the sky is blue",
return "blue is sky the".
"""
def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    return ' '.join(reversed(s.strip().split()))

