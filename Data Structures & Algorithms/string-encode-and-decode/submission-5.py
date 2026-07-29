class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        
        for s in strs:
            strLen = len(s)
            numDigits = len(str(strLen))

            res += (str(numDigits))
            res += (str(strLen))
            res += (s)

        print(res)

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            numDigits = int(s[i])
            i += 1

            strLen = int(s[i : i + numDigits])
            i += numDigits

            res.append(s[i : i + strLen])
            i += strLen

        print(res)

        return res
