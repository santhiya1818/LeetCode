class Solution(object):
    def toHex(self, num):
        if num == 0:
            return "0"
        if num < 0:
            num = (1 << 32) + num
        return hex(num)[2:]
        