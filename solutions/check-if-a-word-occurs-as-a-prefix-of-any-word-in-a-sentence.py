class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        l = sentence.split(' ')
        for i in range(len(l)):
            if l[i].startswith(searchWord):
                return i+1
        return -1
        