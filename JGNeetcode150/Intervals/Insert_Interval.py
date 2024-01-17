class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        print(intervals)
        ans = []
        for i in range(len(intervals)):
            if ans == []:
                ans.append(intervals[i])
            else:
                pre_end = ans[-1][1]
                new_start = intervals[i][0]
                new_end = intervals[i][1]
                if pre_end >= new_start:
                    ans[-1][1] = max(pre_end, new_end)
                else:
                    ans.append(intervals[i])
        return ans