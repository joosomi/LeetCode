class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # return 직원이 일할 수 있는 총 일수  
        # - 미팅 없는 날 count
        # meetings[i] = [start_i, end_i]
        
        # 1. 겹치는 회의 병합 - 새로운 회의 시간표 -> 정렬
        # 2. 종료/시작 시간의 차이 계산, 합산

        # meetings.sort(key=lambda x: x[0])

        meetings.sort()
        merged_meetings = []

        current_start, current_end = meetings[0]   
        for i in range(1, len(meetings)):
            next_start, next_end = meetings[i] 

            # 현재 회의 끝 &  다음 회의 시작 겹치는지 확인 
            if current_end >= next_start:
                current_end = max(current_end, next_end)       
             
            else:
                merged_meetings.append([current_start, current_end])
                current_start, current_end = next_start, next_end
        
        merged_meetings.append([current_start, current_end])
            

        scheduled_days = 0
    
        for start, end in merged_meetings:
            scheduled_days += (end - start + 1)

        return days - scheduled_days
        
        