class Solution:
    def spellchecker(self, wordlist, queries):
        vowels = set('aeiou')

        def devowel(word):
            return ''.join('*' if c in vowels else c for c in word)

        exact = set(wordlist)
        cap_map = {}
        vowel_map = {}

        # Build maps using FIRST occurrence only
        for word in wordlist:
            lower = word.lower()
            masked = devowel(lower)

            if lower not in cap_map:
                cap_map[lower] = word

            if masked not in vowel_map:
                vowel_map[masked] = word

        result = []

        for q in queries:
            if q in exact:
                result.append(q)
                continue

            lower = q.lower()
            masked = devowel(lower)

            if lower in cap_map:
                result.append(cap_map[lower])
            elif masked in vowel_map:
                result.append(vowel_map[masked])
            else:
                result.append("")

        return result
