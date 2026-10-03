class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()                            # sort by start time
        result = [intervals[0]]                     # start with the first interval

        for start, end in intervals[1:]:            # every interval after the first
            lastEnd = result[-1][1]                 # end of the last saved interval
            if start <= lastEnd:                    # overlaps
                result[-1][1] = max(lastEnd, end)   # stretch the last one
            else:
                result.append([start, end])         # no overlap → save as new
        return result