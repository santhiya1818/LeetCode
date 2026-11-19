class Solution(object):
    def checkIfExist(self, arr):
        flag = False
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i != j:
                    if arr[i] == 2*arr[j]:
                        flag = True
        return flag
        