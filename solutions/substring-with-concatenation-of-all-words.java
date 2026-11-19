import java.util.*;

class Solution {

    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> result = new ArrayList<>();

        if (s == null || s.length() == 0 || words == null || words.length == 0)
            return result;

        int wordLength = words[0].length();
        int wordCount = words.length;
        int totalLength = wordLength * wordCount;

        if (s.length() < totalLength)
            return result;

        // Store frequency of each word
        Map<String, Integer> wordMap = new HashMap<>();
        for (String word : words) {
            wordMap.put(word, wordMap.getOrDefault(word, 0) + 1);
        }

        // Try each possible starting offset
        for (int i = 0; i < wordLength; i++) {
            int left = i;
            int count = 0;
            Map<String, Integer> currentMap = new HashMap<>();

            for (int right = i; right + wordLength <= s.length(); right += wordLength) {
                String word = s.substring(right, right + wordLength);

                if (wordMap.containsKey(word)) {
                    currentMap.put(word, currentMap.getOrDefault(word, 0) + 1);
                    count++;

                    while (currentMap.get(word) > wordMap.get(word)) {
                        String leftWord = s.substring(left, left + wordLength);
                        currentMap.put(leftWord, currentMap.get(leftWord) - 1);
                        left += wordLength;
                        count--;
                    }

                    if (count == wordCount) {
                        result.add(left);

                        String leftWord = s.substring(left, left + wordLength);
                        currentMap.put(leftWord, currentMap.get(leftWord) - 1);
                        left += wordLength;
                        count--;
                    }

                } else {
                    currentMap.clear();
                    count = 0;
                    left = right + wordLength;
                }
            }
        }

        return result;
    }
}
