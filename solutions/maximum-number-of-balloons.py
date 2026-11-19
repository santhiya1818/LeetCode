class Solution(object):
    def maxNumberOfBalloons(self, text):
        counts = {
            'b' : text.count('b'),
            'a' : text.count('a'),
            'l' : text.count('l'),
            'o' : text.count('o'),
            'n' : text.count('n')
        }
        counts['l'] //= 2
        counts['o'] //= 2
        return min(counts.values())