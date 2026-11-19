class Solution(object):
    def isPalindrome(self, s):
        st = ""
        for i in s:
            if i.isalnum():
                st+=i
        if st[::].lower() == st[::-1].lower():
            return True
        else:
            return False
        