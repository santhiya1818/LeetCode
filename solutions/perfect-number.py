class Solution(object):
    def checkPerfectNumber(self, num):
        n = 1
        if num<=1:
            return False
        n1 = int(math.sqrt(num))
        for i in range(2,n1+1):
            if num % i == 0:
                n+=i
                if i != num // i:
                    n+= num // i
        return n == num
        