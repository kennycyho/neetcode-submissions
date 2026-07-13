class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> resMap = new HashMap<>();
        for (String str : strs) {

            int[] freq = new int[26];
            for (char c : str.toCharArray()) {
                freq[c - 'a']++;
            }
            String freqStr = Arrays.toString(freq);
            List<String> ls = resMap.getOrDefault(freqStr, new ArrayList<String>());
            ls.add(str);
            resMap.put(freqStr, ls);
        }
        return new ArrayList<>(resMap.values());
    }
}
