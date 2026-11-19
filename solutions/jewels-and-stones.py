class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        cnt = 0
        for i in range(len(jewels)):
            for j in range(len(stones)):
                if jewels[i] == stones[j]:
                    cnt+=1
        return cnt
        