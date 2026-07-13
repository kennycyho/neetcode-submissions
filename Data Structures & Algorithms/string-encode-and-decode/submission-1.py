class Solution:
    def encode(self, strs: List[str]) -> str:
        out = ""
        for word in strs:
            out += f"{len(word)}#{word}"
        print(out)
        return out

    def decode(self, s: str) -> List[str]:
        res = []
        countStr = ""
        count = 0
        word = ""

        for c in s:
            if count > 0:
                word +=  c
                count -= 1
                if count == 0:
                    res.append(word)
                    word = ""
            
            elif c.isnumeric():
                countStr += c

            elif  c == "#":
                count = int(countStr)
                countStr = ""
                if count == 0:
                    res.append("")


        return res
