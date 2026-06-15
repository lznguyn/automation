class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        res = []
        carr = 0

        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 or j >= 0 or carr:
            total = carr

            if i >=0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            res.append(str(total%2))
            carr = total // 2
        return ''.join(res[::-1])