class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # create an empty stack
        # loop through input "operations" - not sure by values or index yet
        # if statement to check if the value is integer it calls stack.push()
        # elif statement that checks if the value is "+" which records a new socore that is the sum of the previous two scores (from the expanded stack which is keeping the scores)
        # elif statement for when the value is "D" which records the double of the previous score
        # elif statement for "C", stack.pop() the previous value
        # return sum(stack) or add all the pop items
        score = []        
        for i in range(len(operations)):
            if operations[i] == "+":
                score.append(score[-1]+score[-2])
            elif operations[i] == "D":
                score.append(score[-1]*2)
            elif operations[i] == "C":
                score.pop()
            else:
                score.append(int(operations[i]))
        print(score)
        return sum(score)