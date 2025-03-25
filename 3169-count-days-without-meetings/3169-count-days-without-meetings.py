class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # return 직원이 일할 수 있는 총 일수  
        # - 미팅 없는 날 count
        # meetings[i] = [start_i, end_i]
        
        # 1. 겹치는 회의 병합 - 새로운 회의 시간표 -> 정렬
        # 2. 종료/시작 시간의 차이 계산, 합산

        # meetings.sort(key=lambda x: x[0])
        meetings.sort()
        print(meetings)
        merged = []

        current = meetings[0]   
        for i in range(1, len(meetings)):
            next_meeting = meetings[i] 

            # 현재 회의 끝 &  다음 회의 시작 겹치는지 확인 
            if current[1] >= next_meeting[0]:
                current = [current[0], max(current[1], next_meeting[1])]             
             
            else:
                if current not in merged:
                    merged.append(current)
                    current = next_meeting
        
        merged.append(current)
            

        print(merged)

        scheduled = 0
    
        for start, end in merged:
            scheduled += (end - start + 1)

        return days - scheduled
        
        