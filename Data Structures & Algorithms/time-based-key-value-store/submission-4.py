class TimeMap:

    def __init__(self):
        self.keyToTimestamp = dict()    # { strKey : { timestamp : strValue } }


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyToTimestamp:
            self.keyToTimestamp[key] = dict()   # { timestamp : strvalue }

        self.keyToTimestamp[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if (key not in self.keyToTimestamp):
            return ""
        
        if timestamp not in self.keyToTimestamp[key]:
            largestTimestamp = -1
            retVal = ""
            for prevTimestamp, value in self.keyToTimestamp[key].items():
                if prevTimestamp <= timestamp and prevTimestamp > largestTimestamp:
                    largestTimestamp = prevTimestamp
                    retVal = value

            return retVal
                    
        return self.keyToTimestamp[key][timestamp]
