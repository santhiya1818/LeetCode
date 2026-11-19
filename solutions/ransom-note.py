class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        flag = True
        for i in range(len(ransomNote)):
            if ransomNote.count(ransomNote[i]) > magazine.count(ransomNote[i]):
                flag = False
        return flag
        