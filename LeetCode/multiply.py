class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                sum_ = mul + result[i + j + 1]
                result[i + j] += sum_ // 10
                result[i + j + 1] = sum_ % 10
        
        # Convert result list to string and remove leading zeros
        result_str = ''.join(map(str, result)).lstrip('0')
        
        return result_str if result_str else '0'
    

# num1 = '12 num2 = '34'
# m = 2, n = 2
# m + n = 4
# result = [0,0,0,0]

# vong lap dau tien i = 1, j = 1
# mul = 2 * 4 = 8
# i + j + 1 = 3
# i + j = 2
# sum_ = 8 + result[3] = 8
# result[2] += 8//10 = 0
# result[3] = 8 % 10 = 8

# => result = [0,0,0,8]

# vong lap thu hai i = 1, j = 0
# mul = 2 * 3 = 6
# i + j + 1 = 2
# i + j = 0
# sum_ = 6 + result[2] = 6
# result[0] += 6//10 = 0
# result[2] = 6 % 10 = 6

# => result = [0,0,6,8]

# vong lap thu ba i = 0, j = 1
# mul = 1 * 4 = 4
# i + j + 1 = 2
# i + j = 0
# sum_ = 4 + result[2] = 10
# result[0] += 10//10 = 1
# result[1] = 10 % 10 = 0

# => result = [1,0,6,8]

# vong lap thu tu i = 0, j = 0
# mul = 1 * 3 = 3
# i + j + 1 = 1
# i + j = 0
# sum_ = 3 + result[1] = 3
# result[0] += 3//10 = 0
# result[1] = 3 % 10 = 3

# => result = [1,3,6,8]