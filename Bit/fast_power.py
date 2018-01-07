"""
(a * b) % p = ((a % p) * (b % p)) % p
将 a^n % b 分解为 (a^(n/2) * a^(n/2) * (a)) %b = ((a^(n/2) * a^(n/2))%b * (a)%b) %b = ((a^(n/2)%b * a^(n/2)%b)%b * (a)%b) %b

"""

class Solution:
    """
    @param: a: A 32bit integer
    @param: b: A 32bit integer
    @param: n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        ans = 1
        while n > 0:
            if n % 2==1:
                ans = ans * a % b
            a = a * a % b
            n = n / 2
        return ans % b