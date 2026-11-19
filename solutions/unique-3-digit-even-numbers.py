class Solution(object):
    def totalNumbers(self, digits):
        s = set()
        n = len(digits)
        for i in range(n):
            if digits[i] == 0:
                continue
            for j in range(n):
                if i ==j:
                    continue
                for k in range(n):
                    if (k != i and k != j and digits[k] %2 == 0):
                        num = digits[i]*100+digits[j]*10+digits[k]
                        s.add(num)
        l1 = list(s)
        l1.sort()
        l2 = len(l1)
        return l2

        