class Solution(object):
    def defangIPaddr(self, address):
        s = ""
        for i in address:
            if i == ".":
                s+="[.]"
            else:
                s+=i
        return s
        