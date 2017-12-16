"""
rotate string:
http://www.lintcode.com/en/problem/rotate-string/
Given "abcdefg".

offset=0 => "abcdefg"
offset=1 => "gabcdef"
offset=2 => "fgabcde"
offset=3 => "efgabcd"

"""

def rotateStr(s, n):
    if s is None or len(s) == 0:
        return s
    l = len(s)
    n %= l
    before = s[0: l-n]
    after = s[l-n: l]
    return after + before

