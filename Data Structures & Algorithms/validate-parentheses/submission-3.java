class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> map = new HashMap();
        map.put(')', '(');
        map.put('}', '{');
        map.put(']', '[');

        LinkedList<Character> q = new LinkedList();
        for (char c : s.toCharArray()) {
            if (map.containsKey(c)) { //is a close bracket
                if (!q.isEmpty() && q.removeLast() == map.get(c)) { //previous bracket is correct
                    continue;
                }
                else {
                    return false;
                }
            }
            else { //is an open bracket
                q.add(c);
            }
        }
        return q.isEmpty();
    }
}
