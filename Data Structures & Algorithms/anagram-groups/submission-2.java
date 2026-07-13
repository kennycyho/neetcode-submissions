class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> resMap = new HashMap<>();
        for (String str : strs) {
            char[] chars = str.toCharArray();
            Arrays.sort(chars);
            String sorted = new String(chars);
            List<String> ls = resMap.getOrDefault(sorted, new ArrayList<String>());
            ls.add(str);
            resMap.put(sorted, ls);
        }
        return new ArrayList<>(resMap.values());
    }
}
