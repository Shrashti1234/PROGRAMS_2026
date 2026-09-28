class Solution:
    def insert(self, intervals, newInterval):
        result = []

        for interval in intervals:

            # Case 1: interval is completely before newInterval
            if interval[1] < newInterval[0]:
                result.append(interval)

            # Case 2: interval overlaps with newInterval
            elif interval[0] <= newInterval[1]:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

            # Case 3: interval is completely after newInterval
            else:
                result.append(newInterval)
                result.extend(intervals[intervals.index(interval):])
                return result

        # Add newInterval if it wasn't added yet
        result.append(newInterval)

        return result