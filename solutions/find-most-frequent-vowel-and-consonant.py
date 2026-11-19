class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq = [0] * 26
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        max_vowel = 0
        max_consonant = 0

        for i in range(26):
            ch = chr(i + ord('a'))
            if ch in vowels:
                max_vowel = max(max_vowel, freq[i])
            else:
                max_consonant = max(max_consonant, freq[i])

        return max_vowel + max_consonant
