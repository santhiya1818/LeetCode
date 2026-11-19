from collections import Counter
from typing import List

class Solution:
    def countPairs(self, words: List[str]) -> int:
        def signature(word: str):
            # Normalize word by shifting all letters based on the first letter
            base = ord(word[0]) - ord('a')
            return tuple((ord(ch) - ord('a') - base) % 26 for ch in word)

        count = Counter(signature(word) for word in words)

        ans = 0
        for freq in count.values():
            ans += freq * (freq - 1) // 2

        return ans