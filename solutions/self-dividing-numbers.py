class Solution(object):
    def selfDividingNumbers(self, left, right):
        n = 0
        l = []
        for i in range(left,right+1):
            flag = True
            n1 = str(i)
            for j in n1:
                if int(j) == 0 or i % int(j) != 0:
                    flag = False
                    break
            if flag:
                l.append(i)
        l = sorted(set(l))
        return l
        