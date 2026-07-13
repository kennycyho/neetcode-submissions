class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<Map, List> resMap = new HashMap<>();
        //foreach string : strs, calculate freqmap
        for (String str : strs) {
            Map<Character, Integer> freq = new HashMap<>();
            for (Character c : str.toCharArray()) {
                freq.put(c, freq.getOrDefault(c, 0) + 1);
            }
            List<String> ls = resMap.getOrDefault(freq, new ArrayList<>());
            ls.add(str);
            resMap.putIfAbsent(freq, ls);
        }
        List<List<String>> res = new ArrayList<>();
        resMap.values().stream().forEach(ls -> res.add(ls));
        return res;
        //if freqmap in key: put in list, else create entry
    }
}
