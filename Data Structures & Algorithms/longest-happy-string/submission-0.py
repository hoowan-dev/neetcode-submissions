class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        if a == b == c == 0:
            return ""

        sol = ""

        prevChars = ['', '']
        while True:
            nextChar = ''

            # greedy approach
            if a >= b and a >= c and a != 0:
                nextChar = 'a'
            elif b >= a and b >= c and b != 0:
                nextChar = 'b'
            elif c >= a and c >= b and c != 0:
                nextChar = 'c'

            if nextChar == '':
                break
     
            # ensure it's not a double dupe
            if nextChar == prevChars[0] and nextChar == prevChars[1]:
                # pick the greatest of the remaining
                if nextChar == 'a':
                    nextChar = ''
                    if b >= c and b != 0:
                        nextChar = 'b'
                    elif c >= b and c != 0:
                        nextChar = 'c'
                elif nextChar == 'b':
                    nextChar = ''
                    if a >= c and a != 0:
                        nextChar = 'a'
                    elif c >= a and c != 0:
                        nextChar = 'c'
                elif nextChar == 'c':
                    nextChar = ''
                    if a >= b and a != 0:
                        nextChar = 'a'
                    elif b >= a and b != 0:
                        nextChar = 'b'

            if nextChar == '':
                break

            if nextChar == 'a':
                a -= 1
            elif nextChar == 'b':
                b -= 1
            elif nextChar == 'c':
                c -= 1

            sol += nextChar
            prevChars[0] = prevChars[1]
            prevChars[1] = nextChar
        
        return sol
