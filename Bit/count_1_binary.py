# 方法1： num & (num-1)每次都可以去掉一个1
# 方法2： >>=通过左移计算最右位是否为1


class Solution:
    """
    @param: num: An integer
    @return: An integer
    """
    def countOnes(self, num):
        cnt = 0
        for x in xrange(32):
            cnt += num & 1
            num >>= 1
        return cnt