class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> bracketMap = Map.of(')', '(', '}', '{', ']', '[');
        Deque<Character> stack = new ArrayDeque<>();
        for (char c : s.toCharArray()) {
            if (bracketMap.containsKey(c)) {
                if (stack.peekLast() == bracketMap.get(c)) stack.removeLast();
                else return false;
            }
            else if (bracketMap.containsValue(c)) stack.addLast(c);
            else continue;
        }
        if (stack.isEmpty()) return true;
        else return false;
    }
}
