class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # answer[i]: i번쨰 날 이후로 더 따뜻한 날이 나타날 때까지 며칠을 기다려야 하는지

        answer = [0] * len(temperatures)
        stack = []

        for index, value in enumerate(temperatures):
            
            while stack and value > stack[-1][1]:
                temp = stack.pop()
                answer[temp[0]] += index - temp[0]

            stack.append((index, value))
        return answer