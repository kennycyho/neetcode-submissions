class Solution {
    public int lengthOfLongestSubstring(String s) {
        int maxLength = 0;
        Set<Character> seen = new HashSet();
        int l = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            while (seen.contains(c)) {
                seen.remove(s.charAt(l));
                l++;
            }
            seen.add(c);
            maxLength = Math.max(maxLength, i - l + 1);
        }
        return maxLength;
    }
}
