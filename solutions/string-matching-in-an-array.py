class Solution(object):
    def stringMatching(self, words):
        a = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    a.append(words[i])
        return list(set(a))
        