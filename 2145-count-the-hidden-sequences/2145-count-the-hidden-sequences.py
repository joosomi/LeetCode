class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # diffrences[i] = hidden[i+1] - hidden[i]
        # - 숨겨진 수열의 연속된 두 수의 차이를 나타냄 
        # - 숨겨진 수열의 각 원소는 lower, upper 사이의 정수 lower <= hidden <= upper

        # 조건을 만족하는 숨겨진 수열의 개수 Return
        # 가능한 수열이 없으면 0 Return

        # (upper - lower + 1, hidden 시작값 x가 될 수 있는 모든 경우의 수) - (range of sequence)
        # 전체 가능한 공간 내에서 hidden 수열 전체 평행 이동을 할 수 있는 개수를 구하면 된다. 

        cases = upper - lower + 1 

        # 틀을 구하기 
        template = [0]

        for i in range(0, len(differences)):
            template.append(template[-1] + differences[i])
            
        range_template = max(template) - min(template) 
        
        print(template)

        ans = cases - range_template

        return  ans if ans > 0 else 0


        