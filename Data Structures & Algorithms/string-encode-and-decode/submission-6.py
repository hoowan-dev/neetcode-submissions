class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for s in strs:
            strLen = len(s)
            encodedStr += (str(strLen) + "/#" + s)

        return encodedStr

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            strLenStr = ""
            while s[i] != '/' and s[i + 1] != '#':
                strLenStr += s[i]
                i += 1

            strLen = int(strLenStr)
            i += 2

            currStr = ""
            for _ in range(strLen):
                currStr += s[i]
                i += 1

            strs.append(currStr)

        return strs