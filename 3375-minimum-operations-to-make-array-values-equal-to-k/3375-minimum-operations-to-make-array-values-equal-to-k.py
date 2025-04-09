class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # 각 인덱스에 대해서 nums[i] > h이면, nums[i]를 h로 바꾼다.
        # 모든 요소가 k와 같아지기 위한 최소 연산 횟수 Return
        # 불가능 -> -1 Return
        # valid integer : h 보다 큰 숫자들이 모두 같은 값인 경우 

        cnt = 0
        n = len(nums)
        nums.sort(reverse=True)
        hs = sorted(set(nums), reverse= True)
        hs.append(k)

        for h in hs:
            greater_than_h = [x for x in nums if x > h]
            if len(set(greater_than_h)) == 1 :
                for i in range(n):
                    if nums[i] > h:
                        nums[i] = h
                cnt +=1
                
            if all(x==k for x in nums):
                return cnt
            
        return -1 
