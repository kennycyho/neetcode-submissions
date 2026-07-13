class Solution:
    def isValidWindow(self, s_freq, t_freq):
        for t, tf in t_freq.items():
            if t not in s_freq:
                return False
            if s_freq[t] < tf:
                return False
        return True
        
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        #constuct freq map for t
        t_freq = {}
        for c in t:
            t_freq[c] = t_freq.get(c, 0) + 1
        print("t_freq="+str(t_freq))
        s_freq = {}
        #move r across s until window is valid
        l = 0
        for r in range(len(s)):
            rc = s[r]
            if rc in t_freq:
                s_freq[rc] = s_freq.get(rc, 0) + 1
            print(f"lc={s[l]}, rc={rc}, s_freq={s_freq}")
            #move l right until just before window is invalid
            while self.isValidWindow(s_freq, t_freq):
                lc = s[l]    
                #save res candidate
                substr = s[l:r+1]
                print(f"substr={substr}")
                res = substr if not res or len(substr) < len(res) else res
                #remove lc
                if lc not in s_freq:
                    pass
                elif s_freq[lc] == 1:
                    s_freq.pop(lc)
                else:
                    s_freq[lc] = s_freq[lc] - 1
                l += 1
        #l++, then repeat steps until r is at end
        return res