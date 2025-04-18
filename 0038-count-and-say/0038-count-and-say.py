class Solution:
    def countAndSay(self, n: int) -> str:
        # def helper() : 연속된 숫자들이 몇 번 나왔는지 [숫자, 개수]

        # def helper() -> 개수 + 숫자 순서로 변경 

        # n-1 번 반복 


        # 연속된 숫자들이 몇 번 나왔는지 => [숫자, 개수] 쌍
        def NumberCount(s):
            res = []
            cnt = 1 
            for i in range(1, len(s)): 
                if s[i]== s[i-1]:
                    cnt +=1
                else: # 다른 경우
                    res.append([s[i-1], cnt])
                    cnt = 1
                
            res.append([s[-1], cnt])
            return res
        

        def to_string(arr):
            for i in range(len(arr)):
                arr[i] = str(arr[i][1]) + arr[i][0]
                
            return "".join(map(str, arr))

        ans = "1"

        for _ in range(n-1):
            res = NumberCount(ans)
            print(res)
            ans = to_string(res)

        return ans 
