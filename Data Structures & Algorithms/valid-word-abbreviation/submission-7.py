class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        wordIndex = 0
        abbrIndex = 0


        #  x
        # internationalization
        #   x
        # i18n

        while ((wordIndex < len(word)) and (abbrIndex < len(abbr))):
            if abbr[abbrIndex].isalpha():
                # compare chars
                if word[wordIndex] != abbr[abbrIndex]:
                    return False
                else:
                    wordIndex += 1
                    abbrIndex += 1
            else:
                if abbr[abbrIndex] == '0':
                    return False

                # gather whole digit
                digitStr = abbr[abbrIndex]
                abbrIndex += 1
                while ((abbrIndex < len(abbr)) and (abbr[abbrIndex].isalpha() == False)):
                    digitStr += abbr[abbrIndex]
                    abbrIndex += 1
                digitInt = int(digitStr)

                for i in range(digitInt):
                    wordIndex += 1
                
        return wordIndex == len(word) and abbrIndex == len(abbr)

