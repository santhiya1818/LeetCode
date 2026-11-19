class Solution(object):
    def detectCapitalUse(self, word):
        cap = 0
        sm = 0
        for i in range(len(word)):
            if ord(word[i]) >= 65 and ord(word[i]) <= 90:
                cap+=1
            elif ord(word[i]) >= 97 and ord(word[i]) <= 122:
                sm +=1
        if ord(word[0]) >= 65 and ord(word[0]) <= 90 and len(word)-1 == sm:
            return True
        if len(word) == cap:
            return True
        if len(word) == sm:
            return True
        return False
        
                