class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0 # XOR 연산에 영향을 줄 수 있는 비트들 

        for i in nums:
            total |= i # OR 연산

        # 2^(n-1) : 전체 부분집합 개수의 절반 
        # 그 비트들은 XOR 연산에 2^(n-1)번 등장
        return total * ( 2**(len(nums)-1))