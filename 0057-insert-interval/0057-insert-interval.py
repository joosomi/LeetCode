class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        intervals.sort()

        left, right = 0, len(intervals)-1

        while left < right:
            mid = (left + right) // 2

            if intervals[mid][1] <= newInterval[1]:
                left = mid + 1 

            else:
                right = mid 

        intervals.insert(left, newInterval)
        
        merged_intervals = []
        for interval in intervals:
            # 끝 < 새로운 인터벌 시작 
            if interval[1] < newInterval[0]:
                merged_intervals.append(interval)
            elif interval[0] > newInterval[1]:
                merged_intervals.append(newInterval)
                newInterval = interval 
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
                
            
        merged_intervals.append(newInterval)

        return merged_intervals