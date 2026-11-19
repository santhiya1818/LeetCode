class Solution(object):
    def digitCount(self, num):
        flag = True
        for i in range(len(num)):
            if num.count(str(i)) != int(num[i]):
                flag = False
                break
        return flag

        