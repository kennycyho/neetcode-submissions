class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> map = new HashMap();
        map.put(')', '(');
        map.put('}', '{');
        map.put(']', '[');

        LinkedList<Character> q = new LinkedList();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (map.keySet().contains(c)) { //is a close bracket
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
