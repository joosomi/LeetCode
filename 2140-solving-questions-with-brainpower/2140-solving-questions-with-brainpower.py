class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # questions[i] = [pointsi, brainpoweri].

        # 문제를 순서대로 처리
        # 문제를 풀지/말지 결정해야 한다.
        # 문제 i를 풀면, 
        # point만큼 점수 but 다음 brainpower개의 문제를  풀 수 없게됨
        # Return 최대 점수를 얻을 수 있는 방법 

        # DP - 각 문제에서 시작했을 때 얻을 수 있는 최대 점수를 저장 
        # dp[i] = 문제 i에서 시작했을 떄 얻을 수 있는 최대 점수
        # - skip 경우: dp[i] = dp[i+1]  
        # - solve 경우: dp[i] = point[i] + dp[i+brainpwower[i] + 1]
        # - dp[i] = max(skip, solve) 현재 문제에서 얻을 수 있는 최대 점수

        dp = [0]*(len(questions) + 1)
      
        for i in range(len(questions)-1, -1, -1):
            
            # skip 
            dp_skip = dp[i+1]
            # solve 
            dp_solve = questions[i][0] 

            if i + questions[i][1] + 1 < len(questions):
                dp_solve = questions[i][0] + dp[i + questions[i][1] + 1]
        

            dp[i] = max(dp_skip, dp_solve)

        return max(dp)

            
         


        