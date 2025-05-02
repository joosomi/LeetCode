class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # 왼쪽으로 넘어지는 도미노는 왼쪽으로 넘어짐
        # 오른쪽으로 넘어지는 도미노는 오른쪽으로 넘어짐
        # 도미노가 양쪽에서 동시에 힘을 받으면, 균형을 받아서 움직이지 않음.

        # Return 도미노들이 최종적으로 어떤 상태가 되는지 

        left_force = [0] * (len(dominoes)+1)
        right_force = [0] * (len(dominoes)+1)

        ans = []

        force = 0
        # 왼 -> 오
        for i in range(len(dominoes)):
            if dominoes[i] == "R":
                force = len(dominoes)
            elif dominoes[i] == "L":
                force = 0
            else:
                force = max(force-1, 0)
            right_force[i] = force
            

        force = 0
        # 오 -> 왼
        for i in range(len(dominoes)-1, -1, -1):
            if dominoes[i] == "L":
                force = len(dominoes)
            elif dominoes[i] == "R":
                force = 0
            else:
                force = max(force-1, 0)
            left_force[i] = force

        for i in range(len(dominoes)):
            if left_force[i] > right_force[i]:
                ans.append("L")
            elif left_force[i] < right_force[i]:
                ans.append("R")
            else:
                ans.append(".")
        return "".join(map(str,ans))