class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        
        numBoats = 0
        i = 0
        j = len(people) - 1

        while i <= j:
            numBoats += 1
            currWeight = people[j]
            j -= 1

            if i <= j and people[i] + currWeight <= limit:
                currWeight += people[i]
                i += 1

        return numBoats