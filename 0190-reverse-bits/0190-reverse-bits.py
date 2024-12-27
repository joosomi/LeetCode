class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        
        ans = 0
        for _ in range(32):
            bit = n & 1
            ans = (ans << 1) | bit # 왼쪽으로 한 칸 이동 + 가장 오른쪽 빈 자리(bit)
            n = n >> 1 # 오른쪽으로 한 칸 이동 - 마지막 비트 제거 

        return ans

        