class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if n < 0:
            x = 1 / x
            n = -n
        result = 1
        current_product = x
        while n > 0:
            if n % 2 == 1:
                result *= current_product
            current_product *= current_product
            n //= 2
        return result



# n = 10
# => 10%2 == 0 => current_product = 2 x 2 = 4 => n //= 2 => n =5
# n = 5
# => 5%2 == 1 => result = 1 x 4 = 4 => current_product = 4 x 4 = 16 => n //= 2 => n = 2
# n = 2
# => 2%2 == 0 => current_product = 16 x 16 = 256 => n //= 2 => n = 1
# n = 1
# => 1%2 == 1 => result = 4 x 256 = 1024 => current_product = 256 x 256 = 65536 => n //= 2 => n = 0
# return 1024

def myPow(self, x, n):
    if n < 0:
        x = 1//x
        n = -n
    res = 1
    curr_pro = x
    while n > 0:
        if n % 2  == 1:
            res *= curr_pro
        curr_pro *= curr_pro
        n //= 2
    return res