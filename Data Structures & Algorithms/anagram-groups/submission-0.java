class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, ArrayList<String>> bins = new HashMap<>();
        for (String word : strs) {
            char[] arr = word.toCharArray();
            Arrays.sort(arr);
            String sortedStr = new String(arr);
            if (!bins.containsKey(sortedStr)) {
                bins.put(sortedStr, new ArrayList<String>());
            }
            bins.get(sortedStr).add(word);
        }
        return new ArrayList<>(bins.values());
    }
}
