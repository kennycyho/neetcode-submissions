class Solution {
    public int lengthOfLongestSubstring(String s) {
        int res = 0;
        char[] chars = s.toCharArray();
        Set<Character> seen = new HashSet<>();
        int l = 0;
        for (int r = 0; r < s.length(); r++) {
            char c = chars[r];
            while (seen.contains(c)) {
                seen.remove(chars[l]);
                l++;
            }
            seen.add(c);
            res = Math.max(res, r - l + 1);
        }
        return res;
    }
}
