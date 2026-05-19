class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        for operation in operations:
            print(records)

            if operation == "+":
                value = records[-1] + records[-2]
                records.append(value)
            elif operation == "D":
                value = records[-1] * 2
                records.append(value)
            elif operation == "C":
                records.pop()
            else:
                value = int(operation)
                records.append(value)

        sum = 0
        for record in records:
            sum += record

        return sum