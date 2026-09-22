class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []                              # stores indices
        result = [0] * len(temperatures)       # default all to 0

        for i, temp in enumerate(temperatures):   # i=index, temp=temperature
            while stack and temp > temperatures[stack[-1]]:
                # found a warmer day!
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)                    # push current index

        return result