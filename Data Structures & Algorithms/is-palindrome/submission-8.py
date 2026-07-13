class Solution:
    def isPalindrome(self, s: str) -> bool:
        #set up left, right pointer on either side
        #while either pointer is on a non alphanum char, move inwards
        #compare left and right character
        #if equal, move inwards
        #continue  l, r pointers pass each other


        l = 0
        r = len(s) - 1

        while l < r:
            while not s[l].isalnum() and l < r:
                l += 1
            while not s[r].isalnum() and l < r:
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True