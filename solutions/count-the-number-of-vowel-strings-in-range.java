class Solution {
    public int vowelStrings(String[] words, int left, int right) {
        return (int) Arrays.stream(words, left, right+1)
.filter(w -> "aeiou".indexOf(w.charAt(0)) >= 0 && "aeiou".indexOf(w.charAt(w.length()-1)) >= 0)
.count();
    }
}